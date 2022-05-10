import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print ctypes.CField
print type(ctypes.Structure._fields_[0][1])

def func(*args):
    print args

ctypes.CFuncPtr = type(func)
print ctypes.CFuncPtr
print type((lambda x: x).func_code)
</code>
I doubt that this will be much of help in practice; you might be better off just searching for <code>ctypes</code> and <code>_ctypes</code> in the source.  For example, if you want the definition of a <code>ctypes.c_int</code>, you might grep for <code>c_int</code>, then look for <code>_ctypes</code>.  If you are looking for something in the <code>_ctypes</code> module, you can just look at the <code>_ctypes</code> subdirectory.

