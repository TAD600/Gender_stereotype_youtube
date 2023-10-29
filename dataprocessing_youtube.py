def main():
    pass

import pandas as pd
import time
import requests
import time
from textblob import Word
import re
from nltk.corpus import stopwords
import spacy
from bs4 import BeautifulSoup


def lowercase_strings(text):
    """
        Converts text data into lowercases. 
        Returns text.  
    """    
    return Word(text).lower()

def remove_punctuation(text):
    
    """
        Removes punctuations in text data. 
        Returns text.  
    """    
    
    return " ".join([Word(word).strip("'" "," "." "!" "?" ";") for word in text.split()])

def remove_newline_special_characters(text):
    
    """
        Removes special and unnecessary characters (e.g., \n, gt) in text data. 
        Returns text.  
    """    
    
    text = text.replace("\n", " ")
    text = text.replace('&gt;', '').replace('gt;', '').replace('gt', '')
    text = re.sub(r'[^\w\s]', '', text)
    return text


def remove_stopwords(text):
    
    """
        Removes English stopwords from nltk package in text data. 
        Returns text.  
    """    
    
    words = text.split()
    words = [word for word in words if word.lower() not in stopwords.words("english") and word.lower() not in ['it39s', 'api', 'ta', 'br', 'pl', 'amp', 'ami', 'amr', 'u', 'tomar', 'moto', 'sob', 'ki', 'kore', 'hoy', 'br']]
    #words = [word for word in words if word.lower() not in stopwords.words("english")]
    return " ".join(words)

def remove_emoticons(text):
    # Define a regular expression pattern to match common emoticons
    emoticon_pattern = r'(?::|;|=)(?:-)?(?:\)|\(|D|P)'

    # Remove emoticons from the text
    text_without_emoticons = re.sub(emoticon_pattern, '', text)

    return text_without_emoticons


import re

def remove_emojis(text):
    # Include the specific emojis you want to remove in the pattern
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F700-\U0001F77F"  # alchemical symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA00-\U0001FA6F"  # Chess Symbols
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        u"\U0001F004-\U0001F0CF"  # Miscellaneous Symbols and Pictographs
        u"\U0001F170-\U0001F251"  # Enclosed Alphanumeric Supplement
        u"\U0001F004-\U0001F0CF"
        u"\U0001F004-\U0001F0CF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1E6-\U0001F1FF"  # flags (iOS)
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F700-\U0001F77F"
        u"\U0001F780-\U0001F7FF"
        u"\U0001F800-\U0001F8FF"
        u"\U0001F900-\U0001F9FF"
        u"\U0001FA00-\U0001FA6F"
        u"\U0001FA70-\U0001FAFF"
        u"\U0001F004-\U0001F0CF"
        u"\U0001F004-\U0001F0CF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1E6-\U0001F1FF"
        
        # Add specific emojis to remove here
        u"\U0001F602"  # 😂
        u"\U0001F389"  # 🎉
        u"\U0001F97A"  # 🥺
        u"\U0001F62D"  # 😭
        u"\U0001F60D"  # 😍
        # Add more emojis to remove here
        
        # Hearts and Flowers
        u"\U00002764"  # ❤️
        u"\U0001F490"  # 💐
        u"\U0001F496"  # 💖
                               
        # Add more hearts, flowers, and other emojis to remove here

        "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(r'', text)



# Loading the spaCy language model
nlp = spacy.load("en_core_web_sm") 

def lemmatize_with_space(text):
    if isinstance(text, str):
        doc = nlp(text)
        lemmatized_words = [token.lemma_ for token in doc]
        return " ".join(lemmatized_words)
    else:
        return text


def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

# parsing date time 
com['time'] = pd.to_datetime(com['Comment Date'], format='%Y-%m-%dT%H:%M:%SZ', errors='coerce')

#dropping the existing index
com.reset_index(drop=True, inplace=True)

# removing the duplicates
comment = comment.drop_duplicates(subset='Comments')

# Remove URLs
comment['Comments'] = comment['Comments'].apply(lambda x: re.sub(r"http\S+", "", str(x)))