import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)


def make_class_method_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(args[0]._impl, *args[1:], **kwargs)
    wrapper.as_c_function = FUNTYPE(wrapper)
    return wrapper


def make_function_wrapper(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        return func(self._impl, *args, **kwargs)
    wrapper.as_c_function = FUNTYPE(wrapper)
    return wrapper


def make_function_wrapper_for_constructor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        impl = func(*args, **kwargs)
        self = args[0].__new__(args[0])
        self._impl = impl
        return self
    wrapper.as_c_function = FUNTYPE(wrapper)
    return wrapper


def make_new_wrapper(func):
    @
