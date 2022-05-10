import ctypes
import ctypes.util
import threading
import sqlite3
import multiprocessing
import logging
import pwd
import grp
import os
import os.path
import shutil
import re
import subprocess
import time
import errno
import base64
import urllib2
import urlparse
import socket
import glob
import psutil
import daemon
import daemon.pidlockfile
import daemon.runner
import daemon.daemoncontext
import daemon.lockfile
import hashlib
import platform

# Set the limit to unlimited
resource.setrlimit(resource.RLIMIT_NOFILE, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

# TODO:
# - Add a dynamic-update option for bind

DB_NAME = None
DB_USER = None
DB_PASS = None
DB_HOST = None
DB_PORT = 3306

DO_DEBUG = False

USE_DAEMON = False

SOCKET_FILE = '/run/powerdns-admin.sock'
SOCKET_PIDFILE = '/run/powerdns-admin.pid'

RUN
