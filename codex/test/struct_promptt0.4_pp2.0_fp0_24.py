import _struct
# Test _struct.Struct.format_size()

import struct
import sys

# A function to test a single format
def test_format(format):
    s = struct.Struct(format)
    expected = len(s.pack(0))
    got = s.format_size()
    if expected != got:
        print("Error: format_size() returned", got, "for format", format)
        print("       Expected", expected)
    else:
        print("format_size() returned", got, "for format", format)

# A function to test all formats
def test_all_formats():
    for format in ['x', 'c', 'b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q',
                   'f', 'd', 's', 'p', 'P']:
        test_format(format)

# A function to test all formats
