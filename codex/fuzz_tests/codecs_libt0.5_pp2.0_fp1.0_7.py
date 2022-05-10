import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import json
import sys
import time
import pymysql
import pymysql.cursors
from datetime import datetime, timedelta

from twisted.enterprise import adbapi
from twisted.internet import reactor, defer
from twisted.python import log
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.media import MediaPipeline
from scrapy.utils.project import get_project_settings
from scrapy import signals

from .items import *

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JsonWithEncodingPipeline(object):
   
