import lzma
lzma.decompress(c)

 
"""
Testing s5_5
"""
print('# print a warning')
print('attention: test this model')

print('# start count')
z = 1
for i in range(10000):
    z = z + 1
print('z = ', z)

"""
Testing P3s
"""

# print
print('print: test this model')
print('print: this is true')

# pprint
from pprint import pprint
from bson.json_util import dumps
from bson import json_util, ObjectId
from json import loads, load
from random import randint
from urllib.request import urlopen
from urllib.error import HTTPError
import json
from collections import defaultdict
from pprint import pprint
from pymongo import MongoClient

from db_ops import start_mongo
from config import get_settings
from logger import *

from datetime import datetime, timezone


from pprint import pprint as p
from textwrap import dedent

from db_ops import start_
