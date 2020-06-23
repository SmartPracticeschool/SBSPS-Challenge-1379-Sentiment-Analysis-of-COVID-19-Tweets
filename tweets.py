import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from textblob import TextBlob
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100 * float(part)/float(whole)
consumer_key = 'e9tqx0vnQ5c9Hc0pEGwhFiknm'
consumer_secret = 'UYZZ7OO5Cwf2VvxR7WCjWTFZJGQ1XravX50VnK34tpEkItCxJB'
access_token = '1261690555911811074-Jv1MRTyrGy6HTvta1HRjHm5TXaAyFk'
access_token_secret ='ETdGFWJlUbqLo7jbHWpR6z73cg6gkGTuNTtBGDcwLAgrw'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
searchTerm =input("Enter keyword to search about :")
noOfSearchTerms= int(input("Enter the number of tweets you want to analyse :"))
tweets = tweepy.Cursor(api.search, q=searchTerm, lang="en").items(noOfSearchTerms)

positive =0
negative=0
neutral=0
polarity=0

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    if(analysis.sentiment.polarity == 0):
        neutral +=1
        
    elif(analysis.sentiment.polarity < 0.00):
        negative +=1
    
    elif(analysis.sentiment.polarity > 0.00):
        positive +=1
        
        
      
positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)


positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("how people are reacting on " + str( searchTerm) + " by analysing"+str(noOfSearchTerms)+" Tweets.")

if(polarity ==0):
    print("neutral sentiments overall")
elif(polarity<0.00):
    print("negative sentiments overall")
elif(polarity>0.00):
    print("positive sentiments overall")  
    
lables = ['Positive[' +str(positive)+'%]','Neutral[' +str(neutral)+'%]','Negative[' +str(negative)+'%]' ]                                         
sizes = [positive, neutral, negative]
colors = ['yellowgreen','gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, lables, loc="best")
plt.axis('equal')
plt.tight_layout                                          
plt.show()                                          
             