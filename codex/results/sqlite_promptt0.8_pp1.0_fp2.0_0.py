import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(:memory:)

# If a sqlite3.Connection object is created using the :memory: database, then that object can only access the in-memory database, not any actual disk file. If you close the connection to the in-memory database and then try to use the Connection object again, an OperationalError exception is raised.

# But, strangely, if you try to connect to a disk file:
#
# db = sqlite3.connect('filename')
# and then execute
#
# c.execute('.open :memory:')
# the :memory: database is opened and the "filename" database is discarded. You can then access the :memory: database using the same cursor or using a different Connection object.
import re
import os
import sys

from sqlalchemy.engine.url import make_url
from sqlalchemy import util
import sqlalchemy

from sqlalchemy import event

from sqlalchemy.pool import NullPool

from sqlalchemy.engine import default
import uuid
import atexit
# import weakref

# import pprint

# import traceback
import logging

import
