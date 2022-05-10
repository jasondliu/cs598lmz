import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def dump(obj):
    print '\n'.join(['%s: %s' % item for item in obj.__dict__.items()])

print 'ctypes.CField:'
dump(ctypes.CField)

print '\nS.x:'
dump(S.x)

print '\nS.x.__class__:'
dump(S.x.__class__)

print '\nS.x.__class__.__bases__:'
print S.x.__class__.__bases__

print '\nS.x.__class__.__base__:'
dump(S.x.__class__.__base__)

print '\nS.x.__class__.__base__.__bases__:'
print S.x.__class__.__base__.__bases__

print '\nS.x.__class__.__base__.__base__:'
dump(S.x.__class__.__base__.__base__)

print '\nS.x
