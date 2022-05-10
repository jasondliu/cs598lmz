import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

if not hasattr(ctypes.CField, "__set__"):
    import _ctypes
    class _set_value(ctypes._set_value):
        class _wrapcmethod(_ctypes._CFuncPtr):
            def from_param(self, arg):
                if ctypes is not None:
                    if isinstance(arg, ctypes.CField):
                        return arg.from_param(arg)
                return _ctypes._CFuncPtr.from_param(self, arg)

        def from_param(self, arg):
            _ctypes._CFuncPtr.from_param(self, arg)
            return self

        def __call__(self, *args):
            args = list(args)
            args[0] = self.offset
            args = tuple(args)
            return self.func(*args)

    class _set_value_for_object(_set_value):
        func = ctypes._CFuncPtr(ctypes._lazydata._set_value_for_object)

    class _set_value_for_address(_set
