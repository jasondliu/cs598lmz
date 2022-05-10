import codecs
# Test codecs.register_error and codecs.lookup_error
import errorcode
import encodings
from encodings import normalize_encoding
from encodings import normalize_encoding as __normalize_encoding
import io
import locale # For BOM
import os
import struct
import sys
import test.support
import traceback

# XXX: _codecs_cn needs a PyUnicode_DecodeUnicodeEscape helper
# to be moved here.

TESTFN = "test1"

def addenc(encoding, info):
    # dictionary keys must be upper case
    encodings.aliases.aliases[encoding.upper()] = info

def testdecode():
    print("Running ", end=' ') ; stdout.flush()
    # test decoding
    f = open(TESTFN, "w")
    try:
        f.write("\xe4\xf6\xfc\xc4\xd6\xdc\xdf")
        f.write("\xe1\xe9\xed\xf3\xfa\xfd\
