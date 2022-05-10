import ctypes
import ctypes.util
import threading
import sqlite3
import re
import time
import sys
import os
import traceback

from . import database
from . import util
from . import config
from . import log

# TODO:
# - add a flag to make it not use the database
# - add a flag to make it not use the database, but still use the cache
# - add a flag to make it not use the database, but still use the cache,
#   and still update the cache
# - add a flag to make it not use the database, but still use the cache,
#   and still update the cache, and still update the database
# - add a flag to make it not use the database, but still use the cache,
#   and still update the cache, and still update the database, but only
#   do the update in the background

# TODO:
# - add a flag to make it use the database, but not update the cache
# - add a flag to make it use the database, but not update the cache,
#   and still update the database
# - add a flag to make it use the database, but not update the cache,
#
