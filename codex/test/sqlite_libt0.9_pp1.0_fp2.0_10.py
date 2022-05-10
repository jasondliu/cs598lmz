import ctypes
import ctypes.util
import threading
import sqlite3
import sqlite3.dbapi2
import sys
import struct
import time

__author__ = "Mircea Ulinic <mircea.ulinic@gmail.com>"
__copyright__ = "Copyright (c) 2012 Mircea Ulinic"
__license__ = "GPL-3+"
__url__ = "http://github.com/pds/pds"


# ----------------------------------------------------------------------

PDS_MALLOC   =  1
PDS_CALLOC   =  2
PDS_REALLOC  =  3
PDS_STRDUP   =  4
PDS_FREE     =  5
PDS_NEW      =  6
PDS_DELETE   =  7
PDS_WCSDUP   =  8
PDS_STACK    =  9
PDS_FUNC     = 10
PDS_MALLOC_SIZE = 11
PDS_CALLOC_N      = 12

