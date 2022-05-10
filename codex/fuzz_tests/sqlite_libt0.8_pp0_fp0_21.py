import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import shutil
import subprocess
import os
import re
import time
import sys
import stat
import atexit
import signal

_REDIS_STATE_KEY = 'redis_state'
_REDIS_AUTH_KEY = 'redis_auth'

(
    REDIS_STATE_OFF,
    REDIS_STATE_ON,
    REDIS_STATE_AUTO
) = range(3)

_state_to_string = {
    REDIS_STATE_OFF: 'off',
    REDIS_STATE_ON: 'on',
    REDIS_STATE_AUTO: 'auto',
}

_string_to_state = {
    'off': REDIS_STATE_OFF,
    'on': REDIS_STATE_ON,
    'auto': REDIS_STATE_AUTO,
}

_SQLITE_PATH = '/home/nobody/sqlite_db/redis_state.db'
_REDIS_DB_FILE = 'dump.rdb'

_REDIS_PORT = 6379
_RED
