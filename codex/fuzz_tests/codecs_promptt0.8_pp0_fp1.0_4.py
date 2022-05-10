import codecs
# Test codecs.register_error()
if (sys.version_info[0] == 2):
	import io
	if io.StringIO == sys.StringIO:
		raise Exception("This version of python is affected by the bug described in CVE-2014-1912 and cannot be used to run certbot tests.")

# Attempt to import python3 modules and downgrade to python2 if possible
warnings.simplefilter("default")
try:
	import http.server as BaseHTTPServer
	import http.client as httplib
	import http.cookies as Cookie
	import urllib.request as urllib2
	import urllib.parse as urlparse
	import socketserver
	import queue
	import configparser as ConfigParser
except ImportError:
	import BaseHTTPServer
	import httplib
	import Cookie
	import urllib2
	import urlparse
	import SocketServer as socketserver
	import Queue as queue
	import ConfigParser

# Set urllib2 timeout to 5 seconds
if (sys.version_info[0] == 2):
	import socket
	socket.setdefaulttimeout
