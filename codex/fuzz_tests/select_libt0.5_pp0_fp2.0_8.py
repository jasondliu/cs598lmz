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

# Cached HTTP responses
http_responses = {
    '/': '<html><body><h1>It works!</h1></body></html>',
    '/index.html': '<html><body><h1>It works!</h1></body></html>',
    '/index.htm': '<html><body><h1>It works!</h1></body></html>',
    '/index.php': '<html><body><h1>It works!</h1></body></html>',
    '/test.html': '<html><body><h1>Test page</h1></body></html>',
    '/test.htm': '<html><body><h1>Test page</h1></body></html>',
    '/test.php': '<html><body><h1>Test page</h1></body></
