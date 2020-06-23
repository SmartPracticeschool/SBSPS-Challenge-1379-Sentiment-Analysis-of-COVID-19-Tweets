import pandas as pd
import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from textblob import TextBlob
import matplotlib.pyplot as plt
 

twitter_consumer_key= 'e9tqx0vnQ5c9Hc0pEGwhFiknm'
twitter_consumer_secret='UYZZ7OO5Cwf2VvxR7WCjWTFZJGQ1XravX50VnK34tpEkItCxJB'

twitter_access_token='1261690555911811074-Jv1MRTyrGy6HTvta1HRjHm5TXaAyFk'

twitter_access_token_secret='ETdGFWJlUbqLo7jbHWpR6z73cg6gkGTuNTtBGDcwLAgrw'

twitter_authentication =tweepy.OAuthHandler(twitter_consumer_key,twitter_consumer_secret)#method of tweepy with unknown code but functionality is in our control, it takes up 2 arguments
twitter_authentication.set_access_token(twitter_access_token,twitter_access_token_secret)
api=tweepy.API(twitter_authentication)
print("Welcome to my application- Twitter_Sentiment_Analysis")

searchTerm ="lockdown"
noOfSearchTerms= 300


public_tweets=tweepy.Cursor(api.search, q=searchTerm, lang="en").items(noOfSearchTerms)

positive=0
negative=0
neutral=0
slightlypositive=0
slightlynegative=0

textList = list()
polarityList= list()
subjectivityList=list()
sentimentList = list()

for tweet in public_tweets:
    txt = tweet.text
    textList.append(txt)
    our_analysis = TextBlob(txt)
    polarity = our_analysis.sentiment.polarity
    subjectivity = our_analysis.sentiment.subjectivity
    Date= tweet.created_at
    
    polarityList.append(polarity)
    subjectivityList.append(subjectivity)
    if(polarity == 0):
        neutral=neutral+1
        sentimentList.append('Neutral')
    elif(polarity <0.00 and polarity>=-0.50):
        slightlynegative=slightlynegative+1
        sentimentList.append('Negative')
    elif(polarity > 0.00 and polarity<=0.50):
        slightlypositive=slightlypositive+1
        sentimentList.append('Positive')    
    elif(polarity < 0.00):
        negative=negative+1
        sentimentList.append('slightlynegative')
    elif(polarity > 0.00):
        positive=positive+1
        sentimentList.append('slightlypositive')     
 
df_data_1 = pd.DataFrame({'Tweet':textList, 'polarity':polarityList, 'subjectivity':subjectivityList, 'Sentiment':sentimentList, 'Date:': Date})
df_data_1.to_csv('twitter_sentiment1.csv', sep=',', encoding='utf-8')
df_data_1.head()

lables = ['Positive[' +str(positive)+'%]','Neutral[' +str(neutral)+'%]','Negative[' +str(negative)+'%]' ,'SlightlyNegative[' +str(slightlynegative)+'%]','SlightlyPositive[' +str(slightlypositive)+'%]']                                         
sizes = [positive, neutral, negative,slightlynegative,slightlypositive]
colors = ['yellowgreen','gold', 'red','g','b']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, lables, loc="best")
plt.axis('equal')
plt.tight_layout                                          
plt.show()     


import matplotlib.pyplot as plt
plt.figure(figsize=(8,6)) 
for i in range(0, df_data_1.shape[0]):
  plt.scatter(df_data_1["polarity"][i], df_data_1["subjectivity"][i], color='Blue') 
# plt.scatter(x,y,color)   
plt.title('Sentiment Analysis') 
plt.xlabel('Polarity') 
plt.ylabel('Subjectivity')  
plt.show()

plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df_data_1['Sentiment'].value_counts().plot(kind = 'bar')
plt.show()

from matplotlib import rcParams
plt.plot(df_data_1.polarity)
plt.plot(df_data_1.subjectivity)
rcParams['figure.figsize'] = 20,6
plt.grid(True)
