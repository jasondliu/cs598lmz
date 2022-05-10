import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import re
import sys
import struct
import math
import argparse
import traceback
import subprocess
import fcntl
import select
import signal
import random
import string
import platform
import shutil
import tempfile
import socket
import ssl
import hashlib
import binascii
import base64

#
# Python 3 compatibility
#

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from BaseHTTPServer import HTTPServer
    from BaseHTTPServer import BaseHTTPRequestHandler

try:
    from socketserver import ThreadingMixIn
except ImportError:
    from SocketServer import ThreadingMixIn

try:
    from queue import Queue
except ImportError:
    from Queue import Queue

