import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
#import mmap
from ..util.sqlite import *
from ..util.common import *
from ..util.log import *
from ..util.mem import *
from .. import internal

logger = logging.getLogger(__name__)

# In memory sqlite database
#sqlite_db = None

# The memory mapped file for the sqlite database
#sqlite_mmap = None

# The file object for the sqlite database
#sqlite_file = None

# The path to the sqlite database
#sqlite_path = None

# The size of the sqlite database
#sqlite_size = 0

# The size of the sqlite database in pages
#sqlite_page_size = 0

# The number of bytes of the sqlite database that are in use
#sqlite_bytes_in_use = 0

# The number of bytes of the sqlite database that are free
#sqlite_bytes_free = 0

# The number of pages that are free
#sqlite_pages_free = 0

# The number
