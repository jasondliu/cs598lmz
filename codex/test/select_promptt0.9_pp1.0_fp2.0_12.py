import select
# Test select.select() in python 2.x and 3.x
if sys.hexversion < 0x03000000: # Python 2.x
  import urllib
  urlopen = urllib.urlopen
  import httplib
  HTTPConnection = httplib.HTTPConnection
  BaseHTTPRequestHandler = BaseHTTPServer.BaseHTTPRequestHandler
else:                         # Python 3.x
  import urllib.request
  urlopen = urllib.request.urlopen
  import http.client
  HTTPConnection = http.client.HTTPConnection
  BaseHTTPRequestHandler = http.server.BaseHTTPRequestHandler
BaseRequestHandler = BaseHTTPRequestHandler
# for easier access, give a different name
from io import BytesIO
stringIO = BytesIO
from io import TextIOWrapper
BufferedReader = TextIOWrapper
# used internally only
from email.message import Message
# For independent serialized clock
import random, time, datetime
# For thread-safe access to shared data
import threading
from queue import Queue
# For detecting error versus expected termination
import traceback

# Python standard
