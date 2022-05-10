import _struct
# Test _struct.Struct access

from struct import error

def get_integer_alignment():
    if _struct.calcsize('i') == _struct.calcsize('l'):
        return 'i'
    elif _struct.calcsize('i') == _struct.calcsize('q'):
        return 'q'
    else:
        raise Exception("don't know what sort of ints this is")

# We can create Struct objects, and pack things with them
S = _struct.Struct("x3s3s")
packed = S.pack("abc", "def")
print packed

# We can't pack unless the number of arguments matches the number
# of format characters
try:
    S = _struct.Struct("x3s3s")
    packed = S.pack("abc", "def", "ghi")
except error:
    print "got expected exception"

# We can't unpack unless the number of format characters matches the length
# of the packed string
try:
    S = _struct.Struct("x3s3s")
    packed = S.unpack("
