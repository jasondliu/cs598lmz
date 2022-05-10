import io
# Test io.RawIOBase

import _io
import os
import sys
import unittest
from test import support
import weakref

# Some useful constants

# A bytes object
TEXT = b'abcdefghijklmnopqrstuvwxyz\n'
# The same, base64-encoded
B64TEXT = b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoK\n'

# A unicode string
UNICODE = '¡¿abcdefghijklmnopqrstuvwxyz\n'

# A unicode string with only ASCII characters
UNICODE_ASCII = 'abcdefghijklmnopqrstuvwxyz\n'

# A unicode string with UTF-16 encoding
UNICODE_UTF16 = (UNICODE.encode('utf-16')[2:] + b'\0\n').decode('utf-16')

# A unicode string with UTF-32 encoding
UNICODE_UTF32 = (UNICODE.en
