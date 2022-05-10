import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()

# 
# fun.__code__
# 
# fun.__code__.co_argcount
# 
# fun.__code__.co_varnames

# fun.__code__.co_argcount

# fun.__code__.co_consts

# fun.__code__.co_consts[0].co_argcount

# fun.__code__.co_consts[0].co_varnames

# fun.__code__.co_consts[0].co_consts

# fun.__code__.co_consts[0].co_consts[0]

# fun.__code__.co_consts[0].co_consts[1]

# fun.__code__.co_consts[0].co_consts[2]

# fun.__code__.co_consts[0].co_consts[3]

# fun.__code__.co_consts[0].co_consts[4]

# fun
