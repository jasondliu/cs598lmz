import _struct
import _ffi

#------------------------------------------------------------------------------
def _gen_decl(rettype, name, argtypes):
    """ Generates CFFI declaration for native function given return type,
    name and argument types list.
    """
    args = ', '.join([_ffi.get_ctype(a) for a in argtypes])
    src = '%s %s(%s)' % (_ffi.get_ctype(rettype), name, args)
    return src

#------------------------------------------------------------------------------
def _get_func_addr(lib, name):
    """ Returns function address by its name.
    """
    return lib.getprocaddress(name)

#------------------------------------------------------------------------------
def _get_func_decl(lib, func):
    """ Returns CFFI declaration of the given function.
    """
    return lib.getcffidecl(func)

#------------------------------------------------------------------------------
class _NativeFunc(object):
    """ Native function wrapper.
    """
    def __init__(self, lib, addr, rettype, name, argtypes):
        """ Constructor.
        """

