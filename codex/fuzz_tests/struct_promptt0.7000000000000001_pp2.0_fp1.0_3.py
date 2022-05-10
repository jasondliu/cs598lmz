import _struct
# Test _struct.Struct

import unittest
from test import test_support

_fmt_header = 'hhl5s'
_fmt_long_header = 'hhh6sh'
_fmt_trailer = 'lh9s'
_fmt_long_trailer = 'lhh10s'

_size_header = _struct.calcsize(_fmt_header)
_size_long_header = _struct.calcsize(_fmt_long_header)
_size_trailer = _struct.calcsize(_fmt_trailer)
_size_long_trailer = _struct.calcsize(_fmt_long_trailer)

_size_short_record = _size_header + _size_trailer
_size_long_record = _size_long_header + _size_long_trailer

_data_short_record = b'2\x00\x00\x00Hello\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
