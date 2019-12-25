import tweepy
import logging
from config import create_api
from dynamoconnect import dynamoget
import time

def main():
    api = create_api()
    message= dynamoget()
    tweet(message,api)
    #tweet("All in is literally be gay do crimes :D", api)

def tweet(message,api):
    try:
        api.update_status(message)
    except tweepy.TweepError:
        print("exception")
        tweet(message+" ",api)
        
    
    
if __name__ == "__main__":
    main()
