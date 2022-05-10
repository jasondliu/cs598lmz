import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import csv
import csv_utils
import datetime
import hashlib
import hmac
import json
import logging
import os
import pdb
import random
import re
import requests
import string
import sys
import time
import uuid
import webapp2
import xml.etree.ElementTree as ET

from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from bs4 import BeautifulSoup
from collections import OrderedDict
from dateutil import parser
from oauth2client.client import SignedJwtAssertionCredentials
from oauth2client.contrib.appengine import OAuth2Decorator
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.appengine import OAuth2DecoratorFromClientSecrets
from pytz import timezone
from random import choice
from time import gmtime,
