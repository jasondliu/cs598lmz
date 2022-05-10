import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Cute(ctypes.Union):
    _anonymous_ = ('s',)
    _fields_ = [('s', S),
                ('value', ctypes.c_int)]

Cute = type(S.value)

print 'c_int    ', ctypes.c_int, ctypes.c_int.__class__
print 'S        ', S, S.__class__
print 'S.x      ', S.x, S.x.__class__, S.x._type_
print 'S        ', S, S.__class__, S._fields_[0]
print 'Cute     ', Cute, Cute.__class__, Cute._fields_[0]
#print 'Cute     ', Cute, Cute._fields_[0][1].__class__, 
print 'Cute._type_', Cute._type_
print 'sizeof(Cute)', ctypes.sizeof(Cute)
print 'type(Cute)', repr(type(Cute))

c = Cute()

#print c
