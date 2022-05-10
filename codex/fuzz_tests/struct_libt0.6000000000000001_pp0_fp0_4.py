import _struct

from _mysql_exceptions import OperationalError, ProgrammingError, IntegrityError, \
     DataError, NotSupportedError
from _mysql_exceptions import Warning, Error, InterfaceError, DatabaseError

from _mysql import string_literal, escape_sequence, escape_dict, escape, \
     escape_string, convert_mysql_timestamp, TIMESTAMP, \
     BINARY, CONNECT, FIELD_TYPE, NUMBER, \
     BLOB, TIMESTAMP, DATE, TIME, DATETIME, NUMBER, STRING, DEFAULT_CURSOR

from _mysql import NULL, version_info, __version__

threadsafety = 1
apilevel = "2.0"
paramstyle = "pyformat"

def debug(x):
	pass

def defaulterrorhandler(connection, cursor, errorclass, errorvalue):
	del connection
	del cursor
	raise errorclass, errorvalue

def warn(msg):
	sys.stderr.write(msg + "\n")

def print_exc(file=None
