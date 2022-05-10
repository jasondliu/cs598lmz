import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def cast(ob):
    if isinstance(ob, ctypes.Array):
        return ob
    return ctypes.cast(ob, ctypes.c_void_p).value # XXX works?

def is_cdata(ob):
    return isinstance(ob, ctypes.Array)

def cdata_pointer(ob):
    return cast(ob)

def cdata_buffer(ob):
    return ctypes.string_at(cast(ob), sizeof(ob))

def cdata_array(ob, size=None):
    addr = cast(ob)
    if size is None:
        size = sizeof(ob)
    # XXX does not work?
    return [ctypes.cast(addr + i, ctypes.c_void_p).value for i in range(size)]

def sizeof(ob):
    if isinstance(ob, ctypes.Array):
        return ob._length_ * ob._type_._length_
    return ctypes.sizeof(ob)

def typeof(ob):
    if isinstance(ob, ctypes
