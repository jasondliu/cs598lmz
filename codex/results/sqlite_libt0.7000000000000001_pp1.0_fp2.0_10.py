import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import sys
import traceback
import time
import re
import random
import configparser

# TODO:
#
#   * Test with different versions of sqlite3.
#   * Test on Windows.
#
# Bugs:
#
#   * Multiple connections to the same database fail.
#   * If you do a SELECT statement on a table, then an INSERT, then
#     a SELECT statement on the same table, the INSERT fails
#     silently.
#
# Things we have to do:
#
#   * We need to check that the filename is valid.
#     - If we get a relative pathname, we need to expand it to an
#       absolute pathname.
#     - We need to check for null bytes.
#     - We may need to check for illegal characters.
#     - We may need to check for path traversal (../../)
#     - If the file exists, we need to check that it is a regular
#       file.
#   * We need to check that the SQL is valid.
#     - We need to check for null
