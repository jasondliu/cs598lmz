import codecs
# Test codecs.register_error()
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# Provides test support for the codecs module.
#
# The tests in this file should pass for all codecs.

# XXX: Fix the tests to use the 'strict' error handler if available.

# Set up the test environment
import testsupport; testsupport.reap_children()

import codecs

# Simple test for the register_error function

def test(name, encoding, errors):

    testcodecs = (
        ('utf_8', 'utf_8', 'utf_8', 'utf_8'),
        ('utf_7', 'utf_7', 'utf_7', 'utf_7'),
        ('unicode_internal', 'unicode_internal', 'unicode_escape', 'unicode_escape'),
        ('latin_1', 'latin_1', 'latin_1', 'latin_1'),
        ('ascii', 'ascii', 'as
