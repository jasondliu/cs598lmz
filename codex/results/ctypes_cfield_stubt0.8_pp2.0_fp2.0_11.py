import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)


class CArrayType(BaseCDataType):
    """
    ctypes array type.
    """
    is_array = True
    is_primitive = False

    def __init__(self, itemtype, length):
        self.itemtype = itemtype
        self.length = length

    def _sizeof(self):
        size = self.itemtype.size
        if rffi.sizeof(lltype.Signed) == 4:
            return ovfcheck(size * self.length)
        else:
            return size * self.length

    def _alignment(self):
        return self.itemtype.alignment

    def _is_pointer_like(self):
        return False

    def _ctype_cache(self):
        return BoolCache
        # the cache is only needed to use BaseCType.set_shape(),
        # but this never happens with CArrayType

    def _create_instance(self, ptr):
        return self.itemtype._create_instance(ptr)

    def newp(self, init):
        return self.
