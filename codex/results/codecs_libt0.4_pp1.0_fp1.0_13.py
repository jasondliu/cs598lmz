import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import logging
import datetime
import traceback
import urllib
import urllib2
import pymongo
import redis
import requests
import bs4

from pymongo import MongoClient
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib import urlencode
from urllib import quote
from urllib import unquote
from urlparse import urlparse
from urlparse import urljoin
from urlparse import parse_qs

from bson.objectid import ObjectId

from django.utils import timezone
from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from apps.core.models import *
from apps.
