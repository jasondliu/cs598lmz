from _struct import Struct
s = Struct.__new__(Struct)
s.size = 8

def pack(self, vals): 
    return b''.join(self.pack(*t) for t in vals) 

s.pack = pack

QQQQ = s.pack(itertools.repeat((1,), 4))

def QQQQ(i): 
    return b'\x01' * 4
