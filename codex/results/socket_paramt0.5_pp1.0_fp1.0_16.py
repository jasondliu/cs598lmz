import socket
socket.if_indextoname('3')

import subprocess
subprocess.check_output(['arp', '-a'])

import sys
sys.stdout.write('Hello World\n')
sys.stdout.flush()

import time
start = time.time()
time.sleep(1)
end = time.time()
print(end - start)

import urllib
urllib.urlopen('http://www.python.org').read()

import wsgiref.handlers
wsgiref.handlers.CGIHandler().run(None)

import xml.dom.minidom
xml.dom.minidom.parseString('<myxml>Some data</myxml>')

import xml.sax
xml.sax.parseString('<myxml>Some data</myxml>', xml.sax.ContentHandler())

import xmlrpclib
xmlrpclib.ServerProxy('http://localhost:8000').add(1, 2)

import zipfile
zipfile.ZipFile('zipfile.zip').read('README.txt')


