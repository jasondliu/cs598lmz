import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import subprocess
import sys
import re
import logging
import socket

# Logging
logging.basicConfig(filename='log.txt',level=logging.ERROR)

# Global variables
global_lock = threading.Lock()
global_db_conn = None
global_db_cursor = None
global_db_filename = ''
global_db_last_modified = 0
global_db_last_size = 0
global_db_last_md5 = ''
global_db_last_sha1 = ''
global_db_last_sha256 = ''
global_db_last_sha512 = ''
global_db_last_crc32 = 0
global_db_last_crc64 = 0
global_db_last_ssdeep = ''
global_db_last_filename = ''
global_db_last_path = ''
global_db_last_extension = ''
global_db_last_size = 0
global_db_last_mime = ''
global_db_last_type = ''
global_db_last_
