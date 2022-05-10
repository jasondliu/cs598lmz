import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import traceback
import subprocess
import re
import json
import datetime
import time
import shutil
import random
import string
import urllib
import urllib2
import hashlib
import base64
import socket
import atexit
import platform
import tempfile

from threading import Thread
from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from urlparse import urlparse, parse_qs
from urllib import urlencode
from subprocess import Popen, PIPE
from shutil import rmtree
from tempfile import mkdtemp
from os.path import join, getsize
from os import listdir, remove, makedirs
from random import randint
from string import ascii_uppercase, digits
from ctypes import *
from ctypes.wintypes import *
from ctypes import wintypes

# Global variables
g_port = 0
g_httpd = None
g_httpd_thread = None
g_db_connection = None
g_db_
