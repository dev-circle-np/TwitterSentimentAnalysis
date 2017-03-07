from keys import consumer_key, consumer_secret
from keys import access_token, access_token_secret
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
    
    key = input('Enter a word to find its sentiment ')
    
    stream = Stream(auth, listener)
    stream.filter(track = [key]) #Add any word you wanna see the sentiment 
                                 #analysis of 
