import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#
#   Logging
#
import logging
from logging.handlers import RotatingFileHandler

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# File handler
file_handler = RotatingFileHandler(
    'tweet_monitoring.log',
    maxBytes=1024*1024*100,
    backupCount=20)
file_handler.setFormatter(formatter)

# Stream handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Get logger
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

#
#   Twitter
#
import tweepy
from tweepy import OAuthHandler
from tweepy import
