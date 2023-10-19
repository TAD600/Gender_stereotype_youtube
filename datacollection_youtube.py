def main():
    pass

import googleapiclient.discovery
from googleapiclient.errors import HttpError
import pandas as pd

def get_comments_from_channels(api_key, channel_ids, max_results=100):
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key
    )

    # Initialize a list to store data
    comments_data = []

    for channel_id in channel_ids:
        # Step 1: Retrieve the list of videos from the channel, including video details
        videos_request = youtube.search().list(
            part="id",
            channelId=channel_id,
            maxResults=max_results,
            type="video"  # Ensure only video results are retrieved
        )
        videos_response = videos_request.execute()

        for video_item in videos_response.get('items', []):
            video_id = video_item['id']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            
            # Get video details
            video_details = get_video_details(api_key, video_id)
            if video_details is not None:
                video_title = video_details.get('title', 'N/A')
            else:
                video_title = 'N/A'
            
            try:
                video_comments_data = get_video_top_level_comments(api_key, channel_id, video_id, max_results)
                for comment_data in video_comments_data:
                    comment_data["Video ID"] = video_id
                    comment_data["Video URL"] = video_url
                    comment_data["Video Title"] = video_title  
                comments_data.extend(video_comments_data)
            except HttpError as e:
                if "comments disabled" in str(e):
                    print(f"Skipping video with comments disabled: {video_id}")
                else:
                    # Handling for videos with comments disabled
                    print(f"Error while fetching comments for video {video_id}: {str(e)}")
                

    # Create a pandas DataFrame from the collected data
    df = pd.DataFrame(comments_data, columns=["Index", "Channel ID", "Commenter ID", "Video ID", "Video URL", "Video Title", "Comment Date", "Comments"])

    return df



def get_video_details(api_key, video_id):
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key
    )

    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )

    response = request.execute()
    if 'items' in response and response['items']:
        video_details = response['items'][0]['snippet']
        return video_details
    return None

def get_video_top_level_comments(api_key, channel_id, video_id, max_results=100):
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key
    )

    # Initialize a list to store data
    video_comments_data = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_results,
            pageToken=next_page_token
        )

        response = request.execute()
        
        for index, item in enumerate(response.get('items', [])):
            comment_data = item['snippet']['topLevelComment']['snippet']
            # Handle KeyError gracefully
            try:
                commenter_id = comment_data['authorChannelId']['value']  # Extract commenter ID
            except KeyError:
                commenter_id = "Unknown"  # Set a default value for commenter ID
            comment_text = comment_data['textDisplay']
            comment_date = comment_data['publishedAt']  # Extract comment date

            # Append the data to the list, including the Video ID, Video URL, and Comment Date
            video_comments_data.append({
                "Index": index,
                "Channel ID": channel_id,
                "Commenter ID": commenter_id,
                "Video ID": video_id,
                "Video URL": f"https://www.youtube.com/watch?v={video_id}",
                "Comment Date": comment_date,
                "Comments": comment_text
            })


  
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return video_comments_data




