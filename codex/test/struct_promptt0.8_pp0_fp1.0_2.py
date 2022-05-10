import _struct
# Test _struct.Struct's arguments
import _struct
import struct
from _struct import error
import sys
from test import support

from test.test_struct import BIG_ENDIAN, LITTLE_ENDIAN, StructTest
from test.support import bigmemtest

# Individual format modules (one for each native format).
# These are loaded dynamically, so that code that imports the
# _struct module can run without being linked against all the
# individual formats.
native_fmts = []
native_fmts_dir = os.path.dirname(__file__) or os.curdir
native_fmts_dir = os.path.join(native_fmts_dir, '_structs')
native_fmts_files = os.listdir(native_fmts_dir)
for fname in native_fmts_files:
    if fname[-3:] != '.py':
        continue
