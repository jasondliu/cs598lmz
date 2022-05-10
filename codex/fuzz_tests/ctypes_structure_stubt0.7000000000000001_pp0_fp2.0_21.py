import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_char

s = S()
S.x.__get__(s)
</code>
This works because of the metaclass <code>StructMeta</code> that the <code>Structure</code> class is subclassing. The <code>__get__</code> method of <code>CField</code> is used as the descriptor.

