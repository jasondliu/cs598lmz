import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import logging
import logging.handlers
import traceback
import requests
import re
import random
import threading
import queue
import urllib.parse
import pymysql
import pymysql.cursors
import pymysql.err
import pymysql.constants.ER
import pymysql.constants.CR
import pymysql.constants.FLAG
import pymysql.constants.CLIENT
import pymysql.constants.COMMAND
import pymysql.connections
import pymysql.connections
import pymysql.connections
import pymysql.connections
import pymysql.connections

from pymysql.connections import Connection
from pymysql.connections import cursors

from pymysql.connections import Cursor
from pymysql.connections import result
