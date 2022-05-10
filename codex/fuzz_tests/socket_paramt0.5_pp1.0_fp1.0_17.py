import socket
socket.if_indextoname(1)

import subprocess
subprocess.call(['ifconfig', 'en0'])

import sys
sys.platform

import urllib
urllib.urlopen('http://www.python.org').read()

import xmlrpclib
server = xmlrpclib.Server('http://localhost:9000')
server.current_time()

import zlib
zlib.compress('This is a test')

import zipfile
zip = zipfile.ZipFile('test.zip', 'w')
zip.write('test.txt')
zip.close()

import zlib
zlib.compress('This is a test')
