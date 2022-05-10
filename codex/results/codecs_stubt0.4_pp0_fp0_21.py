import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

# test_codecs.py
#
# This file tests the codecs module.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# *** Ensure that Python is built with wide Unicode characters ***

import sys
import string
import unittest
import test.support
import io
import codecs
import encodings
import warnings
import weakref

# Some codecs need to be registered for this test to work properly
import encodings.iso8859_1
import encodings.iso8859_15
import encodings.utf_8
import encodings.utf_16
import encodings.utf_16_be
import encodings.utf_16_le
import encodings.utf_32
import encodings.utf_32_be
import encodings.utf_32_le
import encodings.ascii
import encodings.charmap
import encodings.latin_1
import encodings.
