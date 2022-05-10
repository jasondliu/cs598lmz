import _struct
# Test _struct.Struct, and the _struct module
from classes import MyStruct  # Test Struct with methods
import textwrap

# All the parameters below were precomputed using:
# ./python -m test.struct_parameters test_struct

# Test data for simple code values
test_values = [[('x', 'c'), (0, '\x00'), (1, '\1'), (127, '\177'),
                (0xff, '\377')],
               [('h', 'h'), (0, '\x00\x00'), (1, '\x00\x01'),
                (32767, '\x7f\xff'), (0xffff, '\xff\xff')],
               [('H', 'H'), (0, '\x00\x00'), (1, '\x00\x01'),
                (32767, '\xff\x7f'),
                (0xffff, '\xff\xff')],
               [('i', 'i'), (0, '\x00\x00\x00\x00'), (1, '\x00\x00
