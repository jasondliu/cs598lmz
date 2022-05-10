import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import csv

# mysql.connector
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# Twython
from twython import Twython
from twython import TwythonError

# Textblob
from textblob import TextBlob

# OAuth
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# MySql Configuration
config = {
  'user': '',
  'password': '',
  'host': 'localhost',
  'database': '',
  'raise_on_warnings': True,
}

# connect to MySQL
try:
  cnx = mysql.connector.connect(**config)
  # create a cursor
  cursor = cnx.cursor()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS
