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
