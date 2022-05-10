import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def dump_fields(fields):
    for i, (name, type) in enumerate(fields):
        print '%d: %s %s' % (i, name, type)
    print

print 'CField:'
dump_fields(S.x._fields_)

print 'CStruct:'
dump_fields(S._fields_)

print 'CArray:'
dump_fields(ctypes.c_int * 5)

print 'CUnion:'
dump_fields(ctypes.Union)
