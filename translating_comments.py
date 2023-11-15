
def main():
    pass

import requests
import time
from googletrans import Translator
import pandas as pd


# counting the number of videos in one channel, 
filter = comment_b[comment_b['Channel ID'] == 'ABC']
filter['Video ID'].value_counts()


url = "http://example.com"
max_retries = 3
retry_delay = 5  # 5 seconds between retries

for _ in range(max_retries):
    try:
        response = requests.get(url, timeout=10)
        break  # If successful, exit the loop
    except requests.exceptions.ReadTimeout as e:
        print(f"Read operation to {url} timed out. Retrying...")
        time.sleep(retry_delay)  
        
        
def translate_e(text):
    translator = Translator()
    max_retries = 3
    retry_delay = 5  # 5 seconds between retries

    for _ in range(max_retries):
        try:
            translated = translator.translate(text, src='bn', dest='en')
            return translated.text
        except Exception as e:
            print(f"Translation attempt failed. Retrying...")
            time.sleep(retry_delay)

    # If all retries fail, handle the error as failed
    return "Translation failed"


translator = Translator()
def translate_to_english(text):
    translated = translator.translate(text, src='bn', dest='en')
    return translated.text

# for one channel the code should be like this, 
comment_b.loc[comment_b['Channel ID'] == 'ABC', 'Translated_Comments'] = comment_b.loc[comment_b['Channel ID'] == 'ABC', 'Comments'].apply(translate_e) 

# by changing the channel ID's and in case of a channel having thousands of comments, replacing the channel ID with video ID this code has translated the whole Bangla corpus in 4 days running at a stretch.
