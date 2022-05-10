import codecs
# Test codecs.register_error()
import re
import sys
import unittest
import warnings

from test import test_support

# Test data

TESTDATAFILE = test_support.findfile("testdata.txt")

# Encodings

ASCII = "ascii"
UTF8 = "utf-8"
UTF16 = "utf-16"
UTF16_LE = "utf-16-le"
UTF16_BE = "utf-16-be"
UTF32 = "utf-32"
UTF32_LE = "utf-32-le"
UTF32_BE = "utf-32-be"
BZIP2 = "bz2"

# Error handlers

STRICT = "strict"
IGNORE = "ignore"
REPLACE = "replace"
XMLCHARREFREPLACE = "xmlcharrefreplace"
BACKSLASHREPLACE = "backslashreplace"

# Error handler callback functions

def strict_errors(exception):
    raise exception

def ignore_errors(exception):
    pass

def replace_errors(ex
