import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import datetime

from cantools.util import log, logmsg, get_type, timer, args_to_dict
from cantools.web import cgi_dump, cgi_error, serve_static, static_relevant, serve_file, dead, cgi_response, parse_cookie
from cantools.db import put_ctfile, sort

# we create this folder to store uploaded files
# (never share this with anyone)
DB_PATH = "db"

# directory to save http uploads
UPLOAD_PATH = os.path.join(DB_PATH, "uploads")

HOST = "localhost"
PORT = 8082

# modify this to override the google analytics id
GOOGLE_ANALYTICS_ID = None

# api routing/calling on browser
