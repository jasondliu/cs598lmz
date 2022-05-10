from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hh'
s.size = 4

def calcsize(fmt):
    return s.size

class Struct(object):
    def __init__(self, fmt, data=None):
        self.format = fmt
        self.size = calcsize(fmt)
        if data:
            self.pack_into(data)

    def pack_into(self, buf, offset=0):
        pass

def pack(fmt, v1, v2):
    out = cStringIO()
    s = Struct(fmt)
    s.pack_into(out, 0, v1, v2)
    return out.getvalue()

print pack('hh', 1, 2)
</code>
But this gives:
<code>$ python test.py 
test.py:5: DeprecationWarning: _struct.Struct is deprecated, use struct.Struct instead 
  s = Struct.__new__(Struct)
test.py:10: DeprecationWarning: object.__new__() takes no parameters
  s = Struct
