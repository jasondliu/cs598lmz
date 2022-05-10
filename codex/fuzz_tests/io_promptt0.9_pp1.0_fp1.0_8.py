import io
# Test io.RawIOBase
from test import test_support
from test.test_support import run_unittest, TESTFN

from cStringIO import StringIO
from urllib import urlopen
import sys
from os import fdopen
from os import tmpfile
from socket import socket
from thread import *
import unittest
import array

TEST_HTTP_URL = "http://localhost:8002/"
TEST_FTP_URL = "ftp://localhost:8002/"

# Make sure that the states of codepages are the same on all test machines
if sys.platform[:3] not in ('win', 'os2'):
    raise test_support.TestSkipped('The tested codepage is available only on MS platforms')
try:
    u''.encode('ascii')
except LookupError:
    raise test_support.TestSkipped('The "ascii" encoding is required for test')


def print_buffer(buf):
    print >> sys.stderr, "ACTUAL", type(buf)
    try:
        s = buf.getvalue()
   
