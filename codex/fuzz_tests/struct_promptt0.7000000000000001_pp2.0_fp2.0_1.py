import _struct
# Test _struct.Struct

import sys

# This is a list of all the format characters used by the struct module,
# in the order they are mentioned in the module's documentation.
format_chars = 'xcbB?hHiIlLqQfdspP'

# Create all the Struct objects we need for testing.
byte_orders = '@=<>!'
sizes = [1, 2, 4, 8]
byte_order_sizes = [(o, s) for o in byte_orders for s in sizes]
alignments = [True, False]
struct_args = [(c, o + str(s), a)
               for c in format_chars
               for o, s in byte_order_sizes
               for a in alignments]
structs = [apply(struct.Struct, args) for args in struct_args]

def test_format():
    # Test that Struct format string matches the result of using __format__.
    for fmt, s, alignment in struct_args:
        assert fmt == s.__format__('') == s.__format__(' ')

def test
