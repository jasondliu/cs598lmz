import ctypes
# Test ctypes.CField.from_address
if __name__ != '__main__':
    raise ImportError('Only for standalone test')
import ctypes._testcapi

CFieldTestType = ctypes._testcapi.CFieldTestType

CSimpleType = ctypes._testcapi.CSimpleType
# Use a member from the vtable.
# This tests the resolution of member offsets

class VTablePointerHack(ctypes._Pointer):

    def __init__(self, *args, **kw):
        self._obj = None
        ctypes._Pointer.__init__(self, *args, **kw)

    def __ctypes_from_outparam__(self):
        return self


class VTablePointers(object):

    def __init__(self):
        self.f2 = VTablePointerHack(CSimpleType)
        self.f6 = VTablePointerHack(CSimpleType)

if False:
    a1 = self.f2.from_param(vtable.f2)
    a2 = self.f6.from
