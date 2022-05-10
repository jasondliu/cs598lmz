import _struct
import time
import traceback
import base64
import zlib
import pickle
import sys
import os
import threading

try:
    import cPickle as pickle
except ImportError:
    pass

try:
    import hashlib
    sha1 = hashlib.sha1
except ImportError:
    import sha
    sha1 = sha.new

# Timeout in seconds before giving up on a socket read/write
SOCKET_TIMEOUT = 10

# Timeout in seconds before giving up on a lock
LOCK_TIMEOUT = 2

# Timeout in seconds for the server to respond to the initial request
INITIAL_REQUEST_TIMEOUT = 2

# Timeout in seconds for the server to respond to the initial request
INITIAL_REQUEST_TIMEOUT = 2

# Timeout in seconds for the server to respond to a ping request
PING_REQUEST_TIMEOUT = 2

# Timeout in seconds for the server to respond to a set request
SET_REQUEST_TIMEOUT = 1

# Timeout in seconds for the server to
