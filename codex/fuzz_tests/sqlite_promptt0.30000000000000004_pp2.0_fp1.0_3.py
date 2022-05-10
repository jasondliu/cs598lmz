import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import time
import sys
import os
import traceback
import logging

# TODO:
# - Add a check to see if the database is locked.
# - Add a check to see if the database is corrupt.
# - Add a check to see if the database is read-only.
# - Add a check to see if the database is in WAL mode.
# - Add a check to see if the database is in rollback mode.
# - Add a check to see if the database is in auto-vacuum mode.
# - Add a check to see if the database is in incremental-vacuum mode.
# - Add a check to see if the database is in auto-checkpoint mode.
# - Add a check to see if the database is in foreign-key mode.
# - Add a check to see if the database is in write-ahead-log mode.
# - Add a check to see if the database is in shared-cache mode.
# - Add a check to see if the database is in exclusive-locking mode.
# - Add a check to see if the database is in full-fsync
