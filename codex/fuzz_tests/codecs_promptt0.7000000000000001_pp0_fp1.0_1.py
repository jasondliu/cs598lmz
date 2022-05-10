import codecs
# Test codecs.register_error()
import io
import random
import re
import sys
import tempfile
import unittest
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
import zipimport

from test import test_support


# Helper for testing binary I/O
def _check_write(f):
    # Write sample bytes
    f.write(b"abc")
    f.seek(0)
    f.write(b"def")
    f.seek(0)
    f.write(b"gh")
    f.seek(1)
    f.write(b"ij")
    f.seek(0)
    f.write(b"xy")
    f.seek(2)
    f.write(b"z")
    f.seek(0)
    s = f.read()
    f.close()
    return s

# Helper for testing text I/O
def _check_write_w(f):
    # Write sample bytes
    f.write("abc")
    f.seek(0)
    f.write
