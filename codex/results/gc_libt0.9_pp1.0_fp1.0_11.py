import gc, weakref

byteorder = sys.byteorder
if byteorder == 'little':
    def c_long(x): return int(x)
    def c_ulong(x): return int(x)

class WrapperType(type):
    def __new__(cls, name, bases, dict):
        if bytearray not in bases:
            #print "WrapperType.__new__:", name, bases, dict
            dict["__getitem__"]=cls._getitem_
            dict["__mul__"]=cls._mul_
            dict["__rmul__"]=cls._rmul_
            dict["__setitem__"]=cls._setitem_
            dict["__getslice__"]=cls._getslice_
            dict["__setslice__"]=cls._setslice_
        return type.__new__(cls, name, bases, dict)

    @classmethod
    def _getitem_(cls, self, key):
        try:
            return self.memory[key]
        except Type
