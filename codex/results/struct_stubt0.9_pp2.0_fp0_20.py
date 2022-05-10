from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<i 4s f'
s.size = s.calcsize(s.format)
print 'size:', s.size
print 'format:', s.format

try:

    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

data = StringIO("\x12\x34\x56\x78abcdef")
data.seek(0)
unpack_str("<i 4s f", data.read(s.size))
