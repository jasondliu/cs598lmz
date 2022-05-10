import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def is_unbound_cdata(ob):
    return isinstance(ob, (ctypes._CFuncPtr, ctypes.CField))

import ctypes

def memmove_raw(dst, src, length):
    """Like 'memmove', but don't support builtin GC"""
    dst_addr = ctypes.addressof(dst)
    src_addr = ctypes.addressof(src)
    data_addr = ctypes.addressof(dst._objects)
    data = bytearray(data_addr, length)
    data[:length] = data[src_addr - data_addr:src_addr - data_addr + length]
    return dst

def memset_raw(dst, src,  length):
    """Like 'memset', but don't support builtin GC"""
    dst_addr = ctypes.addressof(dst)
    src_addr = ctypes.addressof(src)
    data_addr = ctypes.addressof(dst._objects)
    data = bytear
