import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import logging
import os
import sys
import re
import csv
import time
import json
import datetime
import requests
import MySQLdb
import MySQLdb.cursors
import tweepy

from requests_oauthlib import OAuth1
from tweepy.parsers import JSONParser
from tweepy.streaming import StreamListener

from pytz import timezone

from config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_DATABASE,
    DB_TABLE,
    DB_TABLE_BACKUP,
    DB_TABLE_TMP,
    DB_TABLE_USER,
    DB_TABLE_USER_BACKUP,
    DB_TABLE_USER_TMP,
    DB_TABLE_TWEET,
   
