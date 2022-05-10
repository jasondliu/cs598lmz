import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/Users/zhiyang/Documents/rico/lib/sqlite/db/rico.db')

from sqlite3 import Error
from datetime import datetime
from rico.core.memcached.client import MemcachedClient
from rico.core.redis.client import RedisClient
import rico.core.Task as task
from rico.core.Task import TaskException
from rico.core.Task import TaskState
from rico.core.Task import TaskType
from rico.core.Task import TaskStatus
from rico.core.config import Config
import rico.core.util as util
from rico.core.const import *
from rico.core.const import SEPERATOR

from rico.core.const import _DB_TYPE_SQLITE as _DB_TYPE
from rico.core.const import _DB_TYPE_SQLITE as _DB_TYPE
from rico.core.const import _DB_TYPE_SQLITE as _DB_TYPE
from rico.core.const import _DB_TYPE_SQLITE as _DB_TYPE
from
