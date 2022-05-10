import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import mysql.connector
from mysql.connector import errorcode
import os
import time
import sys
import re
import json
from datetime import datetime
from datetime import timedelta
import calendar
from dateutil.relativedelta import relativedelta
from dateutil import parser
from dateutil import tz
import pytz
from pytz import timezone
import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from oauthlib.oauth2 import TokenExpiredError
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from requests.auth import AuthBase
from urllib.parse import quote
import urllib.parse
import base64
import hmac
import hashlib
import binascii
from twython import Tw
