import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

# -- global varibales --

# DB related
db_path = None
conn = None
cursor = None

# exception-handling related
