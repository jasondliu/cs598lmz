import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import json
import re
import sys
import math
import time
import datetime
import ConfigParser
import MySQLdb
import MySQLdb.cursors
import multiprocessing
import urllib
import requests
import pymongo
import psycopg2
import psycopg2.extras

from time import time,sleep
from random import randrange

from dsid.common import utils
from dsid.common import weights

class WeightProfile():
    """
    """
    def __init__(self, datasource_cfg):
        """
        """
        self.logger = logging.getLogger(__name__)
        
        self.datasource_cfg = datasource_cfg

        self.weighter = None
        if self.datasource_cfg["analyzer_type"] == "PROD":
            self.weighter = weights.ProductWeighter(datasource_cfg)

    def profile_products(self, auth
