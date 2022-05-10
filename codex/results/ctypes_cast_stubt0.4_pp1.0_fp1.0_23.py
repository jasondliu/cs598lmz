import ctypes
ctypes.cast(0, ctypes.py_object).value

#==============================================================================
# The following code is to be deprecated after the 1.0 release
#==============================================================================

try:
    import new
except ImportError:
    new = None

def _get_method_function(method):
    if new is None:
        return method.im_func
    else:
        if not isinstance(method, types.MethodType):
            raise TypeError("argument must be a bound method, not {}".format(
                type(method)))
        return method.__func__

def _get_method_self(method):
    if new is None:
        return method.im_self
    else:
        if not isinstance(method, types.MethodType):
            raise TypeError("argument must be a bound method, not {}".format(
                type(method)))
        return method.__self__

def _create_method(func, self):
    if new is None:
        return new.instancemethod(func, self, type(self))
    else:
        return types.MethodType(
