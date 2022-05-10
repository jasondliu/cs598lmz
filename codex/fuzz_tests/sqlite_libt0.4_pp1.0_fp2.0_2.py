import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import json
import base64
import traceback
import subprocess
import signal
import logging
import logging.handlers
import urllib
import urllib2
import re
import string
import random
import ConfigParser
import hashlib
import datetime
import socket
import struct
import fcntl
import errno
import copy
import random
import uuid
import pwd
import grp

# Global variables
g_config = None
g_logger = None
g_db = None
g_db_lock = threading.Lock()
g_ip_addr = None
g_http_server_port = None
g_http_server_thread = None
g_http_server = None
g_http_server_running = False
g_http_server_stop = False
g_http_server_last_activity = None
g_http_server_last_activity_lock = threading.Lock()
g_http_server_last_activity_timeout = 300
g_http_server_last_activity_timeout_lock = threading
