import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import traceback
import logging
import logging.config

from tqdm import tqdm
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

from pymongo import MongoClient
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from utils import *

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

# 全局变量
ES_HOST = '192.168.1.27'
ES_PORT = 9200

MONGO_HOST = '192.168.1.27'
MONGO_PORT = 27017
MONGO_DB = 'crawler'
MONGO_COLLECTION = 'weibo_user'

# 初始化es
es = Elasticsearch(hosts=ES_HOST
