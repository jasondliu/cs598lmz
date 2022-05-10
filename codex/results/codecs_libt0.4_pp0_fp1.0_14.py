import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import sys
# sys.path.append('../')

import os
import re
import time
import json
import pymysql
import traceback
import datetime
import requests
from urllib import parse

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.http import FormRequest
from scrapy.utils.project import get_project_settings

from db.db_connect import DBConnect
from db.db_handler import DBHandler
from utils.logger import Logger
from utils.common import get_md5
from utils.common import get_keyword
from utils.common import get_url_param
from utils.common import get_url_params
from utils.common import get_url_path
from utils.common import get_url_paths
from utils.common import get_url_last_path
from utils.common import
