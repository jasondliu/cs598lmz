import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CArray(ctypes.Array):
    def _get_item(self, self_addr, index):
        base_addr = self._get_base_addr(self_addr)
        return self._type._type.from_address(base_addr + index * self._type._type.size)

    def _get_base_addr(self, self_addr):
        return ctypes.cast(self_addr, ctypes.POINTER(ctypes.c_void_p)).contents.value


class CType(ctypes.Structure):
    def __getitem__(self, index):
        if isinstance(index, tuple):
            index = index[0]
        return self._type.from_address(self._get_base_addr() + index * self._type.size)

    def _get_base_addr(self):
        return ctypes.cast(ctypes.pointer(self), ctypes.POINTER(ctypes.c_void_p)).contents.value

#class CStruct(ctypes.Structure):
#    def __getitem
