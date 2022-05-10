import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
try:
    fun.__name__
except AttributeError:
    raise Exception('failed to add __name__ to CFUNCTYPE object')
try:
    fun.__doc__
except AttributeError:
    raise Exception('failed to add __doc__ to CFUNCTYPE object')
try:
    fun.__module__
except AttributeError:
    raise Exception('failed to add __module__ to CFUNCTYPE object')

# Issue #15397: ensure that CFUNCTYPE instances can be hashed
fun_hash = hash(fun)
fun_hash

# Issue #15397: ensure that CFUNCTYPE instances can be compared
fun_cmp = fun == fun
fun_cmp

# Issue #15397: ensure that CFUNCTYPE instances can be used as keys in dicts
d = {fun: "test"}
d[fun]

# Issue #15397: ensure that repr() of CFUNCTYPE instances can be executed
repr(fun)

# Issue #15397: ensure that str() of CFUNCTY
