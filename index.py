from keys import consumer_key, consumer_secret, access_token, access_token_secret
from tweepy.streaming import StreamListener
from tweepy import Stream, OAuthHandler
from textblob import TextBlob
import json


class StdOutListener(StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        analysis = TextBlob(decoded['text'])
        print(analysis.sentiment)
        return True
    
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    stream = Stream(auth, listener)
    stream.filter(track = ['']) #Add any word you wanna see the sentiment analysis of 
