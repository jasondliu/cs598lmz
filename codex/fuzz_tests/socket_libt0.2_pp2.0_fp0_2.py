import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version

try:
    import ssl
except ImportError:
    ssl = None

try:
    import selectors
except ImportError:
    selectors = None

try:
    import queue
except ImportError:
    import Queue as queue

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse

try:
    import http.client as httplib
except ImportError:
    import httplib

try:
    import http.cookies as Cookie
except ImportError:
    import Cookie

try:
    import http.cookiejar as cookielib
except ImportError:
    import cookielib

try:
    import email.utils as emailutils
except ImportError:
    import email.Utils as emailutils

try:
    import email.message as emailmessage
except ImportError:
    import email.Message as emailmessage

try:
   
