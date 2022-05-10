import bz2
# Test BZ2Decompressor with a prefilled buffer
import io
import os
import tempfile
import unittest
import bz2_codec
import codecs
import codecs_compat
import filecmp
import unicodedata
ENCODINGS = _available_encodings("bz2")
TESTFN = tempfile.mktemp()


class TestBZ2(unittest.TestCase):

    def test_decompress_lines(self):
        bz2data = b'BZh91AY&SY.1\xe2\x0b$|\x84\x00\x0c\xa0<\x00!\x9ah3M\x96\x00\x08\xc4c\xd2\xdfS:\\\x92\x95tG'
        for params in [{},
            {'encoding': None, 'newline': '\r'},
            {'encoding': None, 'newline': '\r\n'},
            {'encoding': 'utf-8', 'newline': ''},
            {'encoding':
