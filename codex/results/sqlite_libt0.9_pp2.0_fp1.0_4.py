import ctypes
import ctypes.util
import threading
import sqlite3
import yaml
import json
import re
import decimal
import time
import os

# Twilio stuff:
# XXX: fill in your account details and rename to secrets.yaml
with open('secrets.yaml', 'r') as f:
    secrets = yaml.load(f)

account_sid = secrets['account_sid']
auth_token = secrets['auth_token']
my_number = secrets['my_number']

client = TwilioRestClient(account_sid, auth_token)

# Lock to prevent concurrency issues
lock = threading.Lock()

# Constants:
DELIVERY_FAILED_MAX_TIME = 60
FAILOVER_TO_MAX_TIME = 900

# Global functions


def db_query_wrapper(cmd, args=None):
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    try:
        cursor.execute(cmd, args)
        ret = cursor.fetchall()
    except sqlite3.Error, e:
        print "S
