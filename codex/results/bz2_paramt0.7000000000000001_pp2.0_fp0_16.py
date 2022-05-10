from bz2 import BZ2Decompressor
BZ2Decompressor()

from json import JSONDecoder
JSONDecoder()

from zlib import Decompressobj
Decompressobj()

import BaseHTTPServer
BaseHTTPServer.HTTPServer()

# This test makes sure that the new-style classes defined in the
# BaseHTTPServer module are recognized as new-style and do not
# raise an exception when the constructor is called.
import BaseHTTPServer
BaseHTTPServer.BaseHTTPRequestHandler()
BaseHTTPServer.BaseHTTPServer()
BaseHTTPServer.HTTPServer()

import base64
base64.decodestring('')

# This test makes sure that the new-style classes defined in the
# base64 module are recognized as new-style and do not raise an
# exception when the constructor is called.
import base64
base64.Base64()


import binascii
binascii.b2a_base64('')

# This test makes sure that the new-style classes defined in the
# binascii module are recognized as new-style and do not raise an
# exception when
