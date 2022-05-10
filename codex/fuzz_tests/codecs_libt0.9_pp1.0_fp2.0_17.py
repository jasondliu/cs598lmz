import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import ConfigParser

from twitter import *

from mdp import *

from multiprocessing import Value, Pool
from ctypes import c_bool

from db_connections import *
from db_functions import *

from utils import *
from tweet_crawl import *


class TweetCollector:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret, twitter_apl):
        self.tc = TwitterCrawl(consumer_key, consumer_secret, token_key, token_secret, twitter_apl)
        self.tc.twitter_auth()

    """ Retrieve information from user id """
    def get_user_profile(self, user_id, profile_type):

        if '@' in user_id:
            user_info = self.tc.get_twitter_user(user_id)
        else:
            user_info = self.tc.get_twitter_user_by_
