import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def ctypes_typeid(obj):
    """return the 'ctypes type id' for pyobj

    This is the address of the type object as int/long,
    or -1 if the type is not ctypes.
    """
    TP = type(obj)
    try:
        return int(ctypes.addressof(TP))
    except TypeError:
        return -1


class OpaqueType(type):

    def __new__(cls, name, bases, dct):
        self = type.__new__(cls, name, bases, dct)
        self.size = dct['size']
        self._opaque_size = self.size
        self.constructor = False
        self.destructor = False
        return self

    def new(self, builder, op, typos):
        return self(typos)

    def repformat(self):
        supp = self._supported_operations()
        items = [("%s_%s" % (k, self.__name__), v) for k, v in supp.items
