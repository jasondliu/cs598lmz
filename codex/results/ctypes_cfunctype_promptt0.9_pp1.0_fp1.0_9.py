import ctypes
# Test ctypes.CFUNCTYPE for a callback function
def c_callback(func, args, resType=None):

    # A callable result type is used to convert the result in
    # the callback through ctypes.cast.
    class _Holder:
        __value = None

        def set(self, value):
            self.__value = value

        def get(self):
            return(self.__value)

    if(resType is None):
        if(func is None):
            return(None)
        # Result type will be PyObject.
        resType = ctypes.py_object
        res = None
    else:
        # If a result type is specified, then create an
        # instance of the type.
        res = resType()

    def _callback(*args):
        if(args):
            argv = [ctypes.cast(x,ctypes.py_object).value for x in args]
        else:
            argv = []
        # This inner function will be called just befoer
        # the object call. It does a ctypes.cast to the
        # result
