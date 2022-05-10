import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

#TODO:
# - Add support for the following functions:
#   - sqlite3_get_autocommit
#   - sqlite3_db_filename
#   - sqlite3_db_readonly
#   - sqlite3_next_stmt
#   - sqlite3_stmt_readonly
#   - sqlite3_stmt_busy
#   - sqlite3_stmt_status
#   - sqlite3_stmt_isexplain
#   - sqlite3_stmt_readonly
#   - sqlite3_stmt_busy
#   - sqlite3_stmt_status
#   - sqlite3_stmt_isexplain
#   - sqlite3_stmt_isexplain
#   - sqlite3_stmt_isexplain
#   - sqlite3_stmt_isexplain
# - Add support for the following flags:
#   - SQLITE_OPEN_NOMUTEX
#   - SQLITE_OPEN_FULLM
