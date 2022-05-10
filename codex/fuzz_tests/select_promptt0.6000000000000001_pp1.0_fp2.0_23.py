import select
# Test select.select()
import socket
# Test socket.socket()
import sys
import time
# Test time.time()
import traceback
# Test traceback.print_exc()
import types
# Test types.IntType
# Test types.ListType
# Test types.LongType
# Test types.StringType
# Test types.TupleType
import unittest
# Test unittest.assertEquals()
# Test unittest.assertRaises()
# Test unittest.assertTrue()
# Test unittest.TestCase
import urllib
# Test urllib.quote()
# Test urllib.unquote()
# Test urllib.urlencode()
import urllib2
# Test urllib2.urlopen()
import urlparse
# Test urlparse.urlparse()
import weakref
# Test weakref.ref()


__version__ = '$Id$'

#------------------------------------------------------------------------------

# Use the built-in if available, otherwise
# use the Python implementation included in this module.
try:
    from hashlib import md5
except ImportError:
