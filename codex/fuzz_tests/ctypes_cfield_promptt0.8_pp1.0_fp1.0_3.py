import ctypes
# Test ctypes.CField object

class c_fields(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_ulong),
                ]

ts = ctypes.c_ulong.from_buffer(c_fields)

print 'ts.offset ==', ts.offset
print 'ts.size ==', ts.size

class c_invalid(ctypes.Structure):
    pass

try:
    ts = ctypes.c_ulong.from_buffer(c_invalid)
except TypeError, detail:
    print detail
else:
    print ts
    print 'ts.offset ==', ts.offset
    print 'ts.size ==', ts.size

class c_fields(ctypes.Structure):
    pass
c_fields._fields_ = [("a", ctypes.c_int),
                     ("b", ctypes.c_ulong),
                     ]

print ctypes.c_ulong.from_buffer(c_fields)
print 'ts.offset ==', ts.offset

