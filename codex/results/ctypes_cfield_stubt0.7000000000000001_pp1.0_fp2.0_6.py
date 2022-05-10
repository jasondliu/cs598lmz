import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_setattr():
    # ctypes.Structure has no __slots__, but ctypes.c_int has,
    # and ctypes.c_int's __setattr__() is more complicated than
    # the usual one.  So we need to make sure that
    # _wrap_setattr() can call __setattr__() at all.
    py.test.raises(TypeError, "_wrap_setattr(S, 'x', 42)")

def test_wrap_struct_1():
    from pypy.module._rawffi.interp_rawffi import W_DataInstance
    from pypy.module._rawffi.interp_rawffi import new_allocator
    from pypy.rlib.rrawmemory import alloc_raw_storage
    from pypy.rlib.rrawmemory import free_raw_storage
    from pypy.rlib.rrawmemory import cast_adr_to_int
    from pypy.rlib.rrawmemory import cast_int_to_adr
    from p
