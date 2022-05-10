import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared')
import time
import os
import sys
import os.path
import json
import traceback
import logging
import logging.handlers

#DATABASE_NAME = ':memory:'
DATABASE_NAME = 'sqlite.db'

#   CREATE TABLE channels (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(255) NOT NULL,
#     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     UNIQUE (name)
#   );

#   CREATE TABLE users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(255) NOT NULL,
#     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     UNIQUE (name)
#   );

#   CREATE TABLE messages (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     channel_id INTEGER NOT NULL,
#     user_id
