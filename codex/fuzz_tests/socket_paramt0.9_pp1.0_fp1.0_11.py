import socket
socket.if_indextoname("4")

import sys
import urllib2
import httplib
import socks
import time
import random
import binascii
import base64
import struct

from Crypto.Cipher import AES

import util

g_default_user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
g_default_content_type = "application/x-www-form-urlencoded"

# change how you want to connect to the server
def get_http_connection(hostname, port, timeout):
    # not proxy
    return httplib.HTTPConnection(hostname, port = port, timeout = timeout)
    # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1082)
    # return httplib.HTTPConnection(hostname, port = port, timeout = timeout, 
    #     source_address=('127.
