import bz2
bz2.BZ2File

import csv
csv.DictReader

import datetime
datetime.datetime

import email
email.message_from_string

import gzip
gzip.GzipFile

import json
json.dumps

import pickle
pickle.dumps

import subprocess
subprocess.Popen

import urllib
urllib.urlopen

import xml.etree.ElementTree
xml.etree.ElementTree.parse


# These modules are not required by default. However, we would like to
# check them out to see if they are available for use.

try:
    import sqlite3
    sqlite3.connect
except ImportError:
    pass

try:
    import psycopg2
    psycopg2.connect
except ImportError:
    pass

try:
    import pymongo
    pymongo.Connection
except ImportError:
    pass

try:
    import redis
    redis.Redis
except ImportError:
    pass


# XXX: TODO:
