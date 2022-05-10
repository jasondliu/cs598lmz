import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.POINTER(S)

s = S()
print s, type(s), repr(s), s.__dict__ == {'_fields_': ISSUES[8],
                                          '_pack_': 1, '_align_': 'i'}
print s._pack_, s._align_
s.x = 11
s.y = 22
print s.x, s.y
print repr(s.x), repr(s.y)

t = T()
print t, type(t), repr(t), t.__dict__ == {'_fields_': ISSUES[9],
                                          '_pack_': 1, '_align_': 'i'}
print t._pack_, t._align_
t.x = 11
t.y = (s, )
print t.x, t.y

t.y[0].x = 55
print
