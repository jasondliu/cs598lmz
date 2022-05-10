from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2str)
#bz2str.decompress()

#base64decode
from base64 import b64decode
b64decode(base64str)

#regex
import re
re.findall(r'\d+', 'a1b2c3')

#urllib
from urllib.request import urlopen
urlopen('http://www.baidu.com').read()

#urllib2
import urllib.request
urllib.request.urlopen('http://www.baidu.com').read()

#xmlrpc
from xmlrpc.client import ServerProxy
s = ServerProxy('http://127.0.0.1:1234')
s.add(1,2)

#xmlrpclib
import xmlrpclib
s = xmlrpclib.ServerProxy('http://127.0.0.1:1234')
s.add(1,2)

#telnetlib
import telnetlib
t = telnetlib.Telnet
