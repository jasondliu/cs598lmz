import threading
# Test threading daemon
# http://stackoverflow.com/questions/19056107/python-threading-daemon-vs-none

#import urllib2
#import urllib
#import requests
#import json
import re
import time
import datetime
#import lxml.html
#import lxml.etree

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# import MySQLdb
# import mysql.connector

# import MySQLdb.cursors
# import mysql.connector.cursor


# import pymysql
# import pymysql.cursors

# import MySQLdb
# import MySQLdb.cursors

# import pymysql
# import pymysql.cursors

# import sqlite3
# import sqlite3.cursors


class Database:
    def __init__(self, host, user, passwd, db, port=3306, charset='utf8'):
        self.host = host
