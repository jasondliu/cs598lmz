import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import daemon
import lockfile
import socket
import struct
import random
import string
import sqlite3
import gzip
import tarfile
import fcntl
import glob

# CONSTANTS
APP_NAME = 'mainsniffer'
APP_VERSION = '0.2'
DB_FILE = '/usr/sbin/mainsniffer/data.db'
BACKUP_FILE = '/usr/sbin/mainsniffer/data.tar.gz'

BUFSIZE = 128


# Configuration Variables
# If SNI or ALI is not set, then no data will be recorded for that device
SNI_IP = None
SNI_PORT = 60000
SNI_TIMEOUT = 10.0
SNI_CONNECT_TIMEOUT = 1.0
SNI_RETRIES = 3
SNI_ENABLED = True

ALI_IP = None
ALI_PORT = 60001
ALI_TIMEOUT = 10.0
ALI_CONNECT_TIMEOUT = 1.0
AL
