import socket
# Test socket.if_indextoname()
import sys
import test.support
import time
import unittest
import _locale
# Skip tests if _ssl2 is not available.
_ssl2 = test.support.import_module('_ssl2')
ssl = test.support.import_module('ssl')

import asyncore
import asynchat
import pprint
import platform
import weakref

from test import test_support
from test.support import import_module


try:
    import threading
except ImportError:
    threading = None

HOST = test.support.HOST

def hexdump(s):
    return ":".join("{:02x}".format(c) for c in s)

# TLS 1.3 ciphersuites per
# https://tools.ietf.org/html/draft-ietf-tls-tls13-18#appendix-B
TLS13_CIPHER_SUITES = {
    0x1301: {
        "description": "TLS_AES_128_GCM_SHA256",
        "priority": 1
