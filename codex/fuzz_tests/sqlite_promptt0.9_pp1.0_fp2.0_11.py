import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() can open a database.
def test_1():
    con = sqlite3.connect(':memory:')
    cur = con.cursor()
    try:
        cur.execute('select sqlite_version()')
    except:
        raise RuntimeError('Could not connect to in-memory sqlite3 database.')

try:
    import StringIO
except:
    from io import StringIO
try:
    import cPickle
except:
    import pickle as cPickle
from .fcgi_base import *
from . import fcgi_tools
from . import util

from .fcgi_base import fcgi_env

from . import fcgi_base, fcgi_util
from .fcgi_base import fcgi_env
from .fcgi_base import fcgi_tools

from .fcgi_base import fcgi_util
from .fcgi_base import fcgi_tools
from .fcgi_base import fcgi_env


from . import nginx_util
from . import nginx_conf
from .nginx_conf import *
from .ng
