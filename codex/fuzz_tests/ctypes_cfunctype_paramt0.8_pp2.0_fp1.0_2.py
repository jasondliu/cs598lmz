import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def build_cffi_factory(cffi_func):
    @wraps(cffi_func)
    def cffi_factory(*args):
        return cffi_func(*args)
    setattr(cffi_factory, CFFI_FUNC_ATTR, cffi_func)
    return cffi_factory

def build_func(factory, desc, mod_dict, max_arity, mod_dict_build, build_kwargs):
    if max_arity is not None and len(desc[-1]) - 2 > max_arity:
        return
    #print("build_func:", desc)
    # First mode is the tuple (desc,...,kwargs)
    # For this mode, we compare the number of arguments
    # and either dispatch to the next function (if we have too many)
    # or call the cffi function (if we have enough).
    # If no kwargs, we can call the factory directly
    # (no need to put a FunctionWrapper
