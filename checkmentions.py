import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    #new_since_id = since_id
    for tweet in tweepy.Cursor(api.search,
        "StillHereForWonho").items(1):
      try:
            logger.info("Answering to {tweet.user.name}")
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            phrase="Wonho loves you! #StillHereForWonho #절대로_포기는_안해"
            api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
            print ("Replied with " + phrase)
      except tweepy.TweepError as e:
                print(e.reason)

      except StopIteration:
                break
##            api.update_status(
##                status="wonho!!",
##                in_reply_to_status_id=tweet.id,
##            )
    

def main():
    api = create_api()
    since_id = 1
    #print("created")
    api.update_status("WonhoBot found a bug in its script and will work to fix it, if WonhoBot doesn't tweet on time that is why :(")
   # while True:
     #  check_mentions(api, ["#원호사랑해"], since_id)
     #  logger.info("Waiting...")
     #  time.sleep(60)

if __name__ == "__main__":
    main()
