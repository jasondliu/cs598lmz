import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import json
import time
import sys
import re
import datetime
from collections import OrderedDict
from pprint import pprint
from pytz import timezone
import pytz
import tweepy

class TwitterApi(object):
    """
    Class for accessing the Twitter API.
    """

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.stream_listener = StreamListener()
        self.stream = tweepy.Stream(auth=self.api.auth, listener=self.stream_listener)

    def get_tweets(self, query
