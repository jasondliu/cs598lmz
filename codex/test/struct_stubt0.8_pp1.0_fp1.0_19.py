from _struct import Struct
s = Struct.__new__(Struct)
def unpack(data):
    return s.unpack(data)
#end

def customrepr(instance):
    def wrapper(self):
        clsname = type(self).__name__
        items = ["%s=%r"%(f, getattr(self, f)) for f in self._fields_]
        return "%s(%s)"%(clsname, ", ".join(items))
    #end handler

    wrapper.func_name = "__repr__"
    instance.__repr__ = wrapper
#end



class Header(Struct):
    _fmt_ = "!IIII"
    _fields_ = ["magic", "flags", "count", "offset"]
#end class Header

class Node(Struct):
    _fmt_ = "!IIII"
    _fields_ = ["keyoffset", "keylength", "valoffset", "vallength"]
#end class Node

def readblock(self, offset, size):
    self._file.seek(offset)
    return self._file.read(size)
