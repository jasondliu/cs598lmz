import _struct
# Test _struct.Struct

import _struct

# Test struct.__doc__
import struct
assert struct.__doc__ == '\nFunctions to convert between Python values and C structs.\n\nPython values may be integers, floating point numbers, strings, bytes objects,\nlists, tuples or None.\n\nType codes that only differ in the way that they represent integers\n(e.g. \'i\' vs \'I\') are considered equivalent, and in the following\ntable they are shown in grouped together.\n\nIn the table below, \'s\' represents a string, and \'p\' represents a\nPascal string.\n\n+----------------+---------------------------------------------+------------------------------------------+\n| Format | C Type                          | Python type |\n+========+=============================================+==========================================+\n| \'x\'   | pad byte                          | no value    |\n+--------+---------------------------------------------+------------------------------------------+\n| \'c\'   | char                             | bytes of length 1 |\n+--------+---------------------------------------------+------------------------------------------+\n| \'b\'   | signed char                      | integer    |\
