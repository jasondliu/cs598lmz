import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 2

import os
import sys
import time
import signal
import logging
import logging.handlers
import threading
import traceback
import subprocess
import Queue
import socket
import select
import errno
import getpass
import pwd
import grp
import resource
import optparse
import ConfigParser
import re
import tempfile
import shutil
import glob
import pkg_resources

# SOURCE LINE 25

import cherrypy
from cherrypy import _cptools
from cherrypy.lib import auth_digest, auth_basic, httputil, profiler, sessions, static

# SOURCE LINE 29

try:
    import pwd
except ImportError:
    pwd = None
try:
    import grp
except ImportError:
    grp = None

# SOURCE LINE 37

try:
    import win32api
except ImportError:
    win32api = None

# SOURCE LINE 41

try:
    import fcntl
except ImportError:
    f
