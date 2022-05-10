import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

del S

##LITTLE_ENDIAN = 0x0
##BIG_ENDIAN = 0x1

FIELD_OFFSET = (
    ('offset', ctypes.c_byte),
    ('_', ctypes.c_ulonglong, 56),
)

PACK_TO_PACK_SIZE_RATIO = (7, )

class byte_array_guard(bytearray):
    """A guard object to prevent memory corruption

    All python bytes object lives on the GC heap, but raw ctype object lives on
    the native stack. In other word, the memory can be reused any time an
    internal functions return.

    This class is to prevent memory corruption while python bytes object is
    exposed to user, and the corresponding ctype raw buffer can be freed.
    """
    def __init__(self, *args):
        self.buffer = None
        self.field = None
        super().__init__(*args)

    @property
    def raw(self):
        buf = bytearray.__getitem__(self, slice(None))

