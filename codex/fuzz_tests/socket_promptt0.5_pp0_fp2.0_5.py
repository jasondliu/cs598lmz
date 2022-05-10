import socket
# Test socket.if_indextoname
print socket.if_indextoname(1)

import sys
# Test sys.get_inheritable
print sys.get_inheritable(sys.stdin.fileno())

import termios
# Test termios.tcgetattr
print termios.tcgetattr(0)

import thread
# Test thread.allocate_lock
print thread.allocate_lock()

import threading
# Test threading.Lock
print threading.Lock()

import time
# Test time.clock
print time.clock()

import unicodedata
# Test unicodedata.normalize
print unicodedata.normalize('NFKD', u'\u00c5')

import urllib
# Test urllib.urlopen
print urllib.urlopen('http://www.google.com').read()

import urlparse
# Test urlparse.urlparse
print urlparse.urlparse('http://www.google.com')

import uuid
# Test uuid.uuid4
print uuid.uuid4()
