import codecs
# Test codecs.register_error
#
# This test is for the codecs module.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# *** Check the test output for the test results ***

import codecs
import unittest
import sys
import test.support

# Error handlers
class IgnoreTestError(Exception):
    pass

def ignore_errors(exception):
    return (u'', exception.end)

def replace_errors(exception):
    return (u'\ufffd', exception.end)

def xmlcharrefreplace_errors(exception):
    return (u'&#%d;' % ord(exception.object[exception.start]), exception.end)

def backslashreplace_errors(exception):
    return (u'\\x%02x' % ord(exception.object[exception.start]), exception.end)

def strict_errors(exception):
    raise exception

def raise_ignore_errors(exception):
