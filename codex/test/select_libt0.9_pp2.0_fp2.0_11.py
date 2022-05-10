import select
import urllib
import sys
import traceback
import logging
import json
import urllib
import urllib2
import MySQLdb
import pymongo

# Logging
# =======

QUEUE_HOST = MySQLdb.connect(host="kahuna-prod-db.cyrota3gqzq3.us-west-2.rds.amazonaws.com", user="readwrite",passwd='rBiGz7VuMjCzSVYkZp42', db="main")
cursor = QUEUE_HOST.cursor()
cursor.execute('''create table if not exists sms_queue(message varchar(100), phone_number varchar(100), sent int(1), delivery_id varchar(100));''')

cursor.execute('''create table if not exists delivery_confirmations(id varchar(100), message_id varchar(100), sent_at timestamp, sent int(1));''')


MONGO_HOST = 'localhost'
MONGO_PORT
