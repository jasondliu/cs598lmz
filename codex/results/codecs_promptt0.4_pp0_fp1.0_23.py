import codecs
# Test codecs.register_error()
#
# This test is designed to check that codecs.register_error() works
# correctly.  The test is not exhaustive, but should catch most
# problems.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# *** Checked against Unicode 2.0 ***

import unittest
import codecs
import encodings.utf_8
import encodings.utf_16
import encodings.utf_16_le
import encodings.utf_16_be
import encodings.utf_32
import encodings.utf_32_le
import encodings.utf_32_be
import encodings.unicode_internal
import encodings.latin_1
import encodings.ascii
import encodings.base64_codec
import encodings.quopri_codec

# Register the error handler under test

def replace_error(exc):

    if isinstance(exc, UnicodeDecodeError):
