import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import pandas as pd
import requests
import json
import random
from time import sleep
import sys
import csv
from datetime import datetime
from sqlalchemy import create_engine

sys.path.insert(0, '../')

from modules.variables import *

def get_tweets(tweet_ids, tweet_type):
    '''
    Get tweets from the Twitter API by their ids
    '''
    url = 'https://api.twitter.com/1.1/statuses/lookup.json'
    tweets = []

    for id_set in chunker(tweet_ids, 100):
        # get 100 tweets at a time
        id_string = ','.join(str(x) for x in id_set)
        # build url string
        params = {'id': id_string, 'include_entities': 'false', 'tweet_mode': 'extended'}
        try:
            r =
