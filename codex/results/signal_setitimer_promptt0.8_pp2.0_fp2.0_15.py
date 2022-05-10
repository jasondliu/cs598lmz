import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 3, 3)

import thread
import threading
import time
import binascii
import socket
import random
import weakref
import os
import fcntl

import message
import common
import simple_http_client

INVALID_GROUP = message.INVALID_GROUP

# I will play nice, if you don't
# I am sorry, but polipo does not support
# Connection: close
HTTP_REALM = {
  "User-Agent": "Polipo",
  "Accept": "text/html, text/plain, image/*, image/x-xbitmap, image/jpeg, image/pjpeg, */*",
  "Accept-Encoding": "x-gzip, gzip, deflate;q=0.9",
  "Accept-Charset": "ISO-8859-1, utf-8;q=0.66, *;q=0.66",
  "Keep-Alive": "300",
  "Connection": "
