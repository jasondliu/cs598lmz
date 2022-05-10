import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class S2(S):
    y = ctypes.c_int

class S3(S2):
    z = ctypes.c_int()

for cls in 'S', 'S2', 'S3':
    for attr in 'x', 'y', 'z':
        try:
            print cls, attr, getattr(globals()[cls], attr)
        except AttributeError:
            print cls, attr, 'not defined'
</code>
Prints:
<code>S x c_int
S y not defined
S z not defined
S2 x c_int
S2 y c_int
S2 z not defined
S3 x c_int
S3 y c_int
S3 z c_int
</code>

