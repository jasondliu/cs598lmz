import codecs
# Test codecs.register_error() and 'surrogateescape' error handler for
# decoding bytes to Unicode.
# See http://bugs.python.org/issue4180
#
# Written by Marc-Andre Lemburg (mal@egenix.com).
# (c) 2003-2012 eGenix.com Software GmbH; mailto:info@egenix.com
#
# If you find bugs, please report them to <mal@egenix.com>
#
# ************************************************************
# Licensed to PSF under a Contributor Agreement.
# See http://www.python.org/2.4/license for licensing details.
# ************************************************************

import unittest
import sys
import codecs

# unicode strings for testing

utf8_data = u'\u00e4\u00f6\u00fc\u00df' + \
    u'\u6c34\u5e74\u6765\u4e0a\u7ebf' + \
    u'\u30c6\u30b9\u30c8'

utf8_data
