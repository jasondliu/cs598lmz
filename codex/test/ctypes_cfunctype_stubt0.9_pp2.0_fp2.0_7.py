import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

# Get an annotated C error value
def get_error(space):
    return OperationError(space.w_RuntimeError, space.wrap("nop"))
