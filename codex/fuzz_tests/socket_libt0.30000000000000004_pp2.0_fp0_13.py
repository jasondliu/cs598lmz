import socket
import sys
import time
import json
import threading
import random
import os
import logging
import logging.handlers
import traceback
import signal
import subprocess
import re
import pprint
import struct
import base64
import hashlib
import hmac
import urllib
import urllib2
import urlparse
import uuid

#
# Globals
#

#
# Logging
#

logger = logging.getLogger("")

#
# Classes
#

class Server(object):
    def __init__(self, host, port, user, password, name, max_connections):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.name = name
        self.max_connections = max_connections
        self.connections = []
        self.lock = threading.Lock()

    def __str__(self):
        return "%s:%s" % (self.host, self.port)

    def __repr__(self):

