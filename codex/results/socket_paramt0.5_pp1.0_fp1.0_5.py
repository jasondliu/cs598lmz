import socket
socket.if_indextoname(2)

import subprocess
subprocess.call("ifconfig", shell=True)

import sys
sys.platform

import time
print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))

import urllib
urllib.urlopen("http://www.google.com")

import urllib2
urllib2.urlopen("http://www.google.com")

import urlparse
urlparse.urlparse("http://www.google.com")

import uuid
uuid.uuid1()

#import wget
#wget.download("http://www.google.com")

import xmlrpclib
xmlrpclib.ServerProxy("http://www.google.com")

import yaml
yaml.dump({'a':'b'})
