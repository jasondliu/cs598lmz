import ctypes
# Test ctypes.CField class
class mytp(ctypes.Structure):
    _fields_ = [('k', ctypes.c_int),
                ('v', ctypes.c_byte),
                ]

m = mytp()
print(m.k)
print(m.v)
print(m[1])
print(m._pack_)
print([(f[0], f[1].ctype) for f in mytp._fields_])
print([(f[0], f[1].ctype) for f in mytp._fields_])

class ntp(ctypes.Structure):
    _fields_ = [('k', ctypes.c_int),
                ('o', ctypes.c_longlong),
                ]
n = ntp()

class XX(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", (ctypes.c_void_p, 12)),
                ]
print(XX.b.offset)

print(XX.b.offset + XX.a.offset)
print(XX
