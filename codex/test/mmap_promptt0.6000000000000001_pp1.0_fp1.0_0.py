import mmap
# Test mmap.mmap(0, 1, "map", mmap.ACCESS_READ)

import requests

# Test requests.get('http://www.python.org')

import sqlite3
# Test sqlite3.connect(":memory:").cursor()

import ctypes
# Test ctypes.string_at(0)

import hashlib
# Test hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()

import pyexpat
# Test pyexpat.ParserCreate()

import urllib.request, urllib.parse, urllib.error
# Test urllib.request.urlopen('http://www.python.org')

import xmlrpc.client
# Test xmlrpc.client.ServerProxy('http://www.python.org/xmlrpc/').system.listMethods()

import readline
# Test readline.parse_and_bind("tab: complete")

import cProfile
# Test cProfile.run('for i in range(10000): 1+1')

import pstats
# Test pstats.Stats
