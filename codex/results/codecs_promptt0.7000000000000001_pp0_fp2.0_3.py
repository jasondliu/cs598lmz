import codecs
# Test codecs.register_error() and codecs.lookup_error()
import encodings
# Test encodings.aliases.aliases, encodings.aliases.search_function()
# and encodings.normalize_encoding()
import encodings.idna
# Test encodings.idna.ToASCII() and encodings.idna.ToUnicode()
import encodings.utf_8
# Test encodings.utf_8.encode() and encodings.utf_8.decode()
import encodings.unicode_internal
# Test encodings.unicode_internal.decode() and
# encodings.unicode_internal.encode()
import locale
# Test locale.normalize() and locale.setlocale()
import os
import os.path
import struct
# Test struct.unpack()
import sys
import warnings
# Test warnings.filterwarnings() and warnings.warn()
import xml.etree.ElementTree as ET
# Test ElementTree.fromstring()
import xml.sax

from test import support

# Test
