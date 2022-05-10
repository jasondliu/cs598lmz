import _struct
# Test _struct.Struct

# Test alignment
# XXX: This is currently broken.
# struct.calcsize() does not return the correct size for
# non-native byte orders with alignment > 1.
# See http://bugs.python.org/issue1892
# Try to fix this, and remove the following line.
