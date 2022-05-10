import socket
# Test socket.if_indextoname; fails on Mac OS X
socket.if_indextoname(2)

# ctypes
import ctypes
ctypes.ArgumentError

# os.path
import os.path
os.path.basename('/foo/bar')

# xmlrpclib
import xmlrpclib
server = xmlrpclib.ServerProxy('https://www.python.org/pypi')
server.package_releases('demo')

# lxml
import lxml.etree
lxml.etree.parse('')

# pycparser
import pycparser
pycparser.c_parser.CParser

# sqlalchemy
import sqlalchemy
sqlalchemy.String(24)

# httplib
import httplib
h = httplib.HTTPConnection('www.python.org')
h.request('HEAD', '/')
h.getresponse().read()

# subprocess
import subprocess
subprocess.Popen('ls')

# numpy
import numpy
numpy.array([1, 2, 3
