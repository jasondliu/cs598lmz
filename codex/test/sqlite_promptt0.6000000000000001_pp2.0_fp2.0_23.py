import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared')

import sys
from time import sleep
from datetime import datetime

from sqlite4dummy import sqlite4dummy as sqlite

from . import SQLite3TestCase, unittest, skipUnless, skipIf, skip

from . import dbapi2
from .dbapi2 import dbapi2 as sqlite3
from .dbapi2 import threadsafety
from .dbapi2 import StatementCursor
from .dbapi2 import pragma
from .dbapi2 import connect
from .dbapi2 import register_adapter
from .dbapi2 import register_converter
from .dbapi2 import Date
from .dbapi2 import Time
from .dbapi2 import Timestamp
from .dbapi2 import DateFromTicks
from .dbapi2 import TimeFromTicks
from .dbapi2 import TimestampFromTicks
from .dbapi2 import Binary
from .dbapi2 import STRING
from .dbapi2 import BINARY
