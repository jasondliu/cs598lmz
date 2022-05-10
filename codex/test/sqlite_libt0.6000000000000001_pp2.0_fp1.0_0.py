import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

from zope.interface import implements
import zope.event

from twisted.internet import defer, reactor
from twisted.python import log

from allmydata.util import log, iputil, hashutil, fileutil
from allmydata.util.assertutil import precondition
from allmydata.util.fileutil import abspath_expanduser_unicode
from allmydata.interfaces import IStatsProducer
from allmydata.util.encodingutil import listdir_unicode, unicode_to_argv
from allmydata.util.observer import ObserverList

# The maximum number of DB files to keep around.
MAX_OLD_DB_FILES = 5

# The maximum number of DB rows to keep around.
MAX_DB_ROWS = 5000

# The number of seconds to wait between SQLite cleanup operations.
# This has a maximum of 10 minutes and a minimum of 10 seconds.
DB_CLEANUP_DELAY_STEP = 60
DB_CLEANUP_DELAY_MAX = 600
DB_CLEANUP_D
