import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time

from tqdm import tqdm

# Constants
MAX_LINE_LENGTH = 512

# Supported extensions
SUPPORTED_EXTENSIONS = ['mkv', 'mp4', 'm4v', 'mov', 'avi']

# SQL
CREATE_DATABASE = '''
CREATE TABLE IF NOT EXISTS VIDEO (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    HASH TEXT UNIQUE,
    PATH TEXT UNIQUE,
    STATE INTEGER,
    TIMESTAMP INTEGER
);
'''

GET_ALL_VIDEOS = '''
SELECT *
FROM VIDEO
'''

INSERT_OR_UPDATE_VIDEO = '''
INSERT OR IGNORE INTO VIDEO (HASH, PATH, STATE, TIMESTAMP)
VALUES (?, ?, -1, ?)
'''

UPDATE_VIDEO = '''
UPDATE VIDEO
SET STATE = ?
WHERE ID = ?
'''

# Ffmpeg
FFMPEG_BINARY = 'ffmpeg'

