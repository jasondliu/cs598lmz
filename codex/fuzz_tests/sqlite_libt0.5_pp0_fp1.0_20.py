import ctypes
import ctypes.util
import threading
import sqlite3
import os
import shutil
import time

# This is where the db is stored.
DB_PATH = '/var/lib/unifi-video'
DB_NAME = 'unifi-video'

# This is the path to the binary.
UNIFI_VIDEO_PATH = '/usr/sbin/unifi-video'

# This is the path to the sqlite3 binary.
SQLITE3_PATH = '/usr/bin/sqlite3'

# This is the path to the backup directory.
BACKUP_PATH = '/var/backups/unifi-video'

# This is the path to the log file.
LOG_PATH = '/var/log/unifi-video-backup.log'

# This is the number of days to keep backups.
NUM_DAYS = 7

# This is the number of seconds to sleep between checks.
SLEEP_TIME = 300

# This is the number of seconds to wait for the database to be unlocked.
DB_LOCK_TIMEOUT = 30

# This is the number of seconds to wait for the database to be locked
