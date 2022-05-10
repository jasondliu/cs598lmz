import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise ValueError
global_dict = {}
global_dict['fun'] = fun
exec "print fun()" in global_dict
</code>

