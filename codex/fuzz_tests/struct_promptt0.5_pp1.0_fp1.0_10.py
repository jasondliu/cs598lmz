import _struct
# Test _struct.Struct

import unittest
import sys
from test import support

# The values encoded in the test string s.
values = [
    # byte order, size, alignment
    ('@', 1, 'B'),
    ('=', 1, 'B'),
    ('<', 1, 'B'),
    ('>', 1, 'B'),
    ('!', 1, 'B'),
    ('@', 2, 'H'),
    ('=', 2, 'H'),
    ('<', 2, 'H'),
    ('>', 2, 'H'),
    ('!', 2, 'H'),
    ('@', 4, 'I'),
    ('=', 4, 'I'),
    ('<', 4, 'I'),
    ('>', 4, 'I'),
    ('!', 4, 'I'),
    ('@', 4, 'f'),
    ('=', 4, 'f'),
    ('<', 4, 'f'),
    ('>', 4, 'f'),
    ('!', 4, 'f'),
    ('@', 8, 'd'),
    ('=', 8,
