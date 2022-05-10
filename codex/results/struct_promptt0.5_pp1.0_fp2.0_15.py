import _struct
# Test _struct.Struct
try:
    import array
except ImportError:
    array = None

from test import support
from test.support import bigmemtest

# Some structs to test with
struct1 = _struct.Struct('h')
struct2 = _struct.Struct('hh')
struct3 = _struct.Struct('hhh')
struct4 = _struct.Struct('hhhh')
struct5 = _struct.Struct('hhhhh')
struct6 = _struct.Struct('hhhhhh')
struct7 = _struct.Struct('hhhhhhh')
struct8 = _struct.Struct('hhhhhhhh')
struct9 = _struct.Struct('hhhhhhhhh')
struct10 = _struct.Struct('hhhhhhhhhh')
struct11 = _struct.Struct('hhhhhhhhhhh')
struct12 = _struct.Struct('hhhhhhhhhhhh')

# Some byte orders to test with
byte_orders = [
    '@',
    '=',
    '<',
    '>',
    '!',
]

# Some sizes to test with
sizes = [
    1,
    2,
    4,
    8,
