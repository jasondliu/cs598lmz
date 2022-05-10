import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import json
import random
import requests
import datetime
import threading
import traceback
import logging
import logging.handlers
import multiprocessing

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.json_util import loads

from lib.utils import get_now_time
from lib.utils import get_now_time_str
from lib.utils import get_now_time_str_short
from lib.utils import get_now_time_str_short_2
from lib.utils import get_now_time_str_short_3
from lib.utils import get_now_time_str_short_4
from lib.utils import get_now_time_str_short_5
from lib.utils import get_now_time_str_short_6
from lib.utils import get_now_time_str_short_7

