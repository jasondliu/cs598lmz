import _struct

from . import *
from .. import *

class TestUtils(TestCase):
    def test_is_valid_tag(self):
        self.assertTrue(is_valid_tag("0x1"))
        self.assertTrue(is_valid_tag("0x123"))
        self.assertTrue(is_valid_tag("0x12345678"))
        self.assertFalse(is_valid_tag("0x"))
        self.assertFalse(is_valid_tag("0x123456789"))
        self.assertFalse(is_valid_tag("0x123456789abcdef"))
        self.assertFalse(is_valid_tag("0x123456789abcdef0"))
        self.assertFalse(is_valid_tag("0x123456789abcdef0123456789abcdef0"))
        self.assertFalse(is_valid_tag("0x123456789abcdef0123456789abcdef01"))
        self.assertFalse(is_valid_tag("0x123456789abcdef0123456789abc
