def main():
    pass

import time
import pandas as pd
import os
from datetime import datetime 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("stopwords")
nltk.download('vader_lexicon')

from matplotlib.pyplot import figure, cm
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
%matplotlib inline
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

import re
# spacy for lemmatization
import spacy

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)


final = pd.read_csv('Final_Youtube.csv')




# Reference: https://towardsdatascience.com/sentimental-analysis-using-vader-a3415fef7664
sid = SentimentIntensityAnalyzer()
final['Translated_Comments'].fillna('', inplace=True)
# Applying the sentiment analysis function to the 'Translated_Comments' column
final['sentiment_scores'] = final['Translated_Comments'].apply(lambda review: sid.polarity_scores(review))
# Extracting the compound sentiment scores to a new column
final['compound'] = final['sentiment_scores'].apply(lambda score_dict: score_dict['compound'])
final['Sentiment'] = final['compound'].apply(lambda c: 'pos' if c >=0 else 'neg')
mean_sentiment_score = final['compound'].mean()
positive_comments = final[final['compound'] > 0]
num_positive_comments = len(positive_comments)
negative_comments = final[final['compound'] < 0]
num_negative_comments = len(negative_comments)
zero_comments = final[final['compound'] == 0]
num_neutral_comments = len(zero_comments)
num_rows = len(final)

percent_positive_com = (num_positive_comments / num_rows) * 100
percent_negative_com = (num_negative_comments / num_rows) * 100
percent_neutral_com = (num_neutral_comments/ num_rows) * 100
print(num_rows)
print(f'Number of positive comments: {num_positive_comments} ({percent_positive_com:.2f}%)')
print(f'Number of negative comments: {num_negative_comments} ({percent_negative_com:.2f}%)')
print(f'Number of zero comments: {num_neutral_comments} ({percent_neutral_com:.2f}%)')

#Visuals:

labels = ['Positive', 'Negative', 'Neutral']
sizes = [percent_positive_com, percent_negative_com, percent_neutral_com]
plt.figure(figsize=(3,3))

# Pie Chart
plt.pie(sizes, labels = labels,autopct='%1.2f%%', colors=sns.color_palette('Set2'))
plt.axis('equal')
plt.show()

final['date'] = pd.to_datetime(final['date'])  
final['year'] = final['date'].dt.year  

# Line plot
grouped = final.groupby('year')['compound'].mean()
grouped = final.pivot_table(index='year', columns=None, values='compound', aggfunc='mean')
grouped_gender= final.groupby(['year', 'gender'])['compound'].mean().unstack()
cmm = pd.concat([grouped, grouped_gender], axis=1)
# Reference: https://www.kdnuggets.com/2022/11/4-ways-rename-pandas-columns.html
cmm.rename(columns={"compound": "Overall"}, inplace=True)
cmm.rename(columns={0: "Male"}, inplace=True)
cmm.rename(columns={1: "Female"}, inplace=True)

lines = cmm.plot.line()
# Customize the plot
#plt.title("Public sentiment over the Years regarding artists in YouTube", fontsize= 12)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Mean sentiment score per year", fontsize=10)
plt.legend(["Overall", "Male", "Female"], loc='upper right')
plt.xticks(cmm.index, rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

com.to_csv("Final_Youtube.csv", encoding='utf-8', index=False)





