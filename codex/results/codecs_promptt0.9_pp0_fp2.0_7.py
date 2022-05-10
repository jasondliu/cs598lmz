import codecs
# Test codecs.register_error()

from test import test_support
import re
from test.test_support import run_unittest
from cStringIO import StringIO
import sys
from encodings import ascii
import encodings.string_escape
import encodings.hex_codec
from encodings import utf_7, utf_8, utf_16, utf_16_le, utf_16_be\
     , unicode_escape
from encodings import base64_codec
from encodings import charmap
from encodings import palmos, cp037
from encodings import cp1006, cp273
from encodings import cp424, cp437, cp500, cp720
from encodings import cp737, cp775, cp856, cp857
from encodings import cp858, cp860, cp861, cp862
from encodings import cp863, cp864, cp865, cp866
from encodings import cp869, cp874
from encodings import cp875, cp932, cp949, cp
