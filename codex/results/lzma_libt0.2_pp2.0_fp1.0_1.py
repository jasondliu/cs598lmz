import lzma
lzma.LZMAError

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest

import pyximport
pyximport.install()

import cython_lzma

class TestCythonLzma(unittest.TestCase):
    def test_compress(self):
        data = b'1234567890'
        compressed = cython_lzma.compress(data)
        self.assertEqual(data, cython_lzma.decompress(compressed))

    def test_compress_with_dict(self):
        data = b'1234567890'
        compressed = cython_lzma.compress(data, dict_size=1 << 20)
        self.assertEqual(data,
