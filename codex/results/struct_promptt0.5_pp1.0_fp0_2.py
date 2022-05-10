import _struct
# Test _struct.Struct.
packed = _struct.pack('hhl', 1, 2, 3)
print(_struct.unpack('hhl', packed))
# Test _struct.error.
try:
    _struct.pack('hhh', 1, 2)
except _struct.error as msg:
    print(msg)

# Test array.array.
from array import array
a = array('i', [0, 1, 2, 3, 4])
print(a[1:3])

# Test repr.
print(repr(set('supercalifragilisticexpialidocious')))

# Test pprint.
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
pprint.pprint(t, width=30)

# Test textwrap.
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc,
