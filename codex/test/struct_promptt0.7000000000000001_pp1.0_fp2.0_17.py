import _struct
# Test _struct.Struct()
from test import test_support
import unittest

from collections import namedtuple

pack_t = namedtuple('pack', 'code s')
size_t = namedtuple('size', 'code s')

