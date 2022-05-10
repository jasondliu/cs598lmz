import codecs
# Test codecs.register_error
#
# (C) 2001-2011 Chris Liechti <cliechti@gmx.net>
# this is distributed under a free software license, see license.txt

import codecs
import unittest

#-----------------------------------------------------------------------------

class Test_register_error(unittest.TestCase):

    def test_strict(self):
        self.assertRaises(UnicodeDecodeError, codecs.decode, b'\x80', 'ascii')

    def test_ignore(self):
        self.assertEqual(
            codecs.decode(b'\x80', 'ascii', 'ignore'),
            (u"", 1))

    def test_replace(self):
        self.assertEqual(
            codecs.decode(b'\x80', 'ascii', 'replace'),
            (u"\ufffd", 1))

