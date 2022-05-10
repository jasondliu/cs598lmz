import mmap
import os
import re
import subprocess
import sys
import time
import traceback

from optparse import OptionParser

from pymongo import MongoClient

from bson.objectid import ObjectId
from datetime import datetime, timedelta

from mongo_utils import get_mongo_uri_from_config

class Statsd(object):
    """
    Statsd class which can be used to send stats to the statsd server.
    """

    def __init__(self, host, port, prefix=''):
        """
        Initialize the statsd class.

        :Parameters:
            - `host`: the statsd host
            - `port`: the statsd port
            - `prefix`: the prefix to send before the stats name
        """
        self.host = host
        self.port = port
        self.prefix = prefix

    def send(self, stat, value, rate=1):
        """
        Send a stats value to the statsd server.

        :Parameters:
            - `stat`: the stat name
            - `value`:
