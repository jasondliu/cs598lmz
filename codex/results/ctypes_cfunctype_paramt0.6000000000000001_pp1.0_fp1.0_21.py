import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def get_f(name, opts=()):
    """
    Get the function named name from the module named in the
    _FUNCTION_MODULE_NAME attribute of the current class. 
    """
    if name not in self._functions:
        module = __import__(self._FUNCTION_MODULE_NAME, globals(), locals(), [name])
        cfunc = getattr(module, name)
        self._functions[name] = FUNTYPE(cfunc)
    return self._functions[name]
</code>
This is in a class, the class has a <code>_functions</code> attribute which is a <code>{}</code> and a <code>_FUNCTION_MODULE_NAME</code> attribute which is a string.
The problem is that the call to <code>getattr(module, name)</code> never returns any function objects.
edit:
I am trying to get the function from a library, so the <code>_FUNCTION_MODULE_NAME</code> is set to the
