import codecs
codecs.register_error("strict", codecs.ignore_errors)

import os
import re

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def get_tweets(username):
    """
    Get a user's tweets and write them to a file.
    """
    dirname = username
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    filename = username + '.txt'

    #tweets = [status for status in tweepy.Cursor(api.user_timeline, id=username).items()]
    #for tweet in tweets:
    #    print tweet.text

    with open(os.path.join(dirname, filename), 'wb') as f:
        for status in
