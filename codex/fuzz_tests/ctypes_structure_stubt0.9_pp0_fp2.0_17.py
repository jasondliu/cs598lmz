import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("a", ctypes.c_byte, 4), 
                ("b", ctypes.c_byte, 2),
                ("c", ctypes.c_byte, 2)]
    def f(self):
        print self.a, self.b, self.c

.field private static final a:B
.field private static final b:B
.field private static final c:B
.method static constructor <clinit>()V
    .limit locals 1
    .limit stack 0
    ldc 0x1
    putstatic S.a:B
    ldc 0x2
    putstatic S.b:B
    ldc 0x4
    putstatic S.c:B
    return
</code>
Python doesn't know how to deal with this structure (yet?), so it doesn't know how to convert it to C.
What you can do is "convert" it manually, either do the shifting and masking yourself, use the _pack_ and _unpack_ methods (or the struct module), or use the Union class which can share values between fields and normal attributes
