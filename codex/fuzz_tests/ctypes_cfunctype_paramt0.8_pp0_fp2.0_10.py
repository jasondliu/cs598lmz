import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def define_c_function(signature):
    return FUNTYPE(signature)

def wrap_c_function(f):
    # Note that we need to return a function that accepts a
    # NumbaFunctionObject, not just a NumbaFunctionObject. This is because
    # it is the signature of the calling function that will be used, not the
    # signature of the callee.
    sig = f.signature.as_ctypes()
    def call_cfunc(funobj):
        arg_list = [funobj.func_globals[arg] for arg in funobj.signature.args]
        return f(*arg_list)
    call_cfunc.cfunc = ctypes.CFUNCTYPE(sig)(call_cfunc)
    return call_cfunc

def call_c_function(f, signature, args):
    args = [arg.box_get() for arg in args]
    sig = signature.as_ctypes()
    cfunc = ctypes.CFUNCTYPE(s
