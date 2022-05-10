import _struct
# Test _struct.Struct()
from test import test_support
import unittest

from collections import namedtuple

pack_t = namedtuple('pack', 'code s')
size_t = namedtuple('size', 'code s')

class StructTest(unittest.TestCase):

    def test_struct(self):
        cases = [
            ('=bBhHiIqQfd',
             pack_t('b', chr(1)),
             pack_t('B', 1),
             pack_t('h', -2),
             pack_t('H', 2),
             pack_t('i', -3),
             pack_t('I', 3),
             pack_t('q', -4),
             pack_t('Q', 4),
             pack_t('f', 1.0),
             pack_t('d', 2.0)),
            ('s',
             pack_t('s', 'abcdefghijklmnop'),
             pack_t('s', 'abcdefghijklmnopp'),
             pack_t('s', 'abcdefghijkl
