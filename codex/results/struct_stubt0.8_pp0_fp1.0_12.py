from _struct import Struct
s = Struct.__new__(Struct)
#s = Struct("!f", float("nan")).unpack(open("test.dat", 'rb').read())[0]
s.format = "!f"
s.size = 4
try:
    s.unpack(open("test.dat", 'rb').read())
except Error, msg:
    print msg

# NOTE: We may want this to work; it's not clear whether it should.  The
# difference is that the C code enforces alignment whereas the python code
# doesn't.
#_struct.unpack("!f", bytes)
