import select
import socket
import sys
import time
import urllib2

# Global settings
HOST = 'localhost'
PORT = 8080
TIMEOUT = 1

# Global variables
http_headers = ''
http_body = ''

