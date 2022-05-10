import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
# the rpython.rtyper.extregistry.ExtRegistryEntry
# linked to this function uses a special hack:
# we don't want to do a forced cast to 
