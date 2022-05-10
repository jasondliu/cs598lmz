import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

import json
import os
import re
import tweepy
import pymysql
os.chdir('/home/limeng/CUT/twitter/')

def create_api():
    consumer_key = CON_KEY
    consumer_secret = CON_SEC
    access_token = ACC_TOK
    access_token_secret= ACC_SEC
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        print(e)
        pass
    print('API Created')
    return api

api = create_api()
connect = pymysql.connect(host='###',db
