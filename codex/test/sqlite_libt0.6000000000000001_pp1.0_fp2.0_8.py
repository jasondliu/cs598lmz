import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import re
import time
import datetime
from datetime import datetime
from datetime import timedelta
import traceback

from sqlite3 import OperationalError
from sqlite3 import ProgrammingError

import pylibmc
from pylibmc import Client

from configobj import ConfigObj

import logging
import logging.handlers

import re
import urllib
import urllib2
import urlparse

import json

import argparse

import pygeoip

from collections import defaultdict

import time

from pprint import pprint

import socket

from pymongo import MongoClient

from bson.objectid import ObjectId

from bson.json_util import dumps

from bson.code import Code

from bson.son import SON

import gzip

import bz2

import lzma

import string

from gzipstream import GzipStreamFile


def get_data_type(data):
    if isinstance(data, basestring):
        return 'string'

