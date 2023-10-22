
def main():
    pass


from langdetect import detect

def categorize_language(comment):
    """a function to categorize comments"""
    try:
        detected_language = detect(comment)
        if detected_language == 'bn':
            return 'Bangla'
        elif detected_language == 'en':
            return 'English'
        else:
            return 'Bangla-English Mixed'
    except:
        return 'Unknown'
  



