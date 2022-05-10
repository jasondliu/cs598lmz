import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

from . import _sqlite
from . import _sqlite3
from . import util

try:
    from . import _sqlite3_ext
except ImportError:
    pass

try:
    from . import _sqlite3_ext_json1
except ImportError:
    pass

try:
    from . import _sqlite3_ext_fts4
except ImportError:
    pass

try:
    from . import _sqlite3_ext_fts5
except ImportError:
    pass

try:
    from . import _sqlite3_ext_rtree
except ImportError:
    pass

try:
    from . import _sqlite3_ext_icu
except ImportError:
    pass

try:
    from . import _sqlite3_ext_misc
except ImportError:
    pass

try:
    from . import _sqlite3_ext_stat4
except ImportError:
    pass

try:
    from . import _sqlite3_ext_pcre
except ImportError:
   
