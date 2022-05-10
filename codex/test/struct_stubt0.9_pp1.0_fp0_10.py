from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'xcbHi'
s.size = struct.calcsize(s.format)
 
class Header(namedtuple('Header', 'command device action flags modifier key button x y x_root y_root')):
    __slots__ = ()
    def __new__(cls, data):
        return super(Header, cls).__new__(cls, *s.unpack(data[:s.size]))

from struct import pack, unpack
p = pack(s.format, 97, 0, 3, 0, 0, 49, 0, 0, 0)
print(Header(p))
try:
    print(p[:s.size], len(p[:s.size]))
    print(Header(p[:s.size]))
except:
    print(traceback.format_exc())
b = p[s.size:]
