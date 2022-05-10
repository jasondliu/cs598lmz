import ctypes
import ctypes.util
import threading
import sqlite3
from struct import *

# import idaapi
import idc
import idautils
from idaapi import *
from idc import *
from idautils import *

"""
    Structure of .ida/db/ida.sqlite3
    -------------------------------
    xrefs (table)
    - id (integer, primary key)
    - src (integer)
    - dst (integer)
    - type (integer)
    - ord (integer)
"""

# path to sqlite db
sqlite_db = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ida.sqlite3')

# sqlite3 connection and cursor
conn = sqlite3.connect(sqlite_db)
c = conn.cursor()

# ida api, idaapi
ida_api = None
ida_api_t = None

# idc api, ida.hpp
idc_api = None
idc_api_t = None

# idautils api, idp.hpp, idd
