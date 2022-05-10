import threading
threading.stack_size(2**27)
import sys
import inspect

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

from datetime import date, timedelta

def main():

    def printTweet(descr, t):
        print(descr)
        print("Username: %s" % t.username)
        print("Retweets: %d" % t.retweets)
        print("Text: %s" % t.text)
        print("Mentions: %s" % t.mentions)
        print("Hashtags: %s\n" % t.hashtags)

    # Example 1 - Get tweets by username
    tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

    printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)

    # Example 2 - Get tweets by query search
   
