import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# import psycopg2

# silence QueryInterface warnings from V8
warnings.filterwarnings('ignore', '.*queryInterface.*', RuntimeWarning,
	'sqlalchemy.sql.elements')
warnings.filterwarnings('ignore', '.*queryInterface.*', Warning,
	'sqlalchemy.sql.elements')

# silence dialect warnings
warnings.filterwarnings('ignore', '.*dialects.*', RuntimeWarning)

# silence warnings about unknown table options, coming from sqlite3.connect
warnings.filterwarnings('ignore', '.*unknown table option.*', RuntimeWarning,
	'sqlalchemy.dialects.sqlite.base')
warnings.filterwarnings('ignore', '.*unknown table option.*', Warning,
	'sqlalchemy.dialects.sqlite.base')

log.warn("DEPRECATED: Please import sqlalchemy.dialects.sqlite instead. "
         "The current package name is deprecated due to "
         "confusion with native sqlite dialects.")

libdatesupport = ctypes.util.find_
