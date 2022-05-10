fn = lambda: None
# Test fn.__code__.co_argcount, fn.__code__.co_flags and use
# ctypes.pythonapi.PyCode_NewEmpty to convert it to something we can
# look at (w00t!)
class func(FunctionType):
    def __init__(self, *args, **kwds):
        FunctionType.__init__(self, *args, **kwds)
        self.__code__ = ctypes.pythonapi.PyCode_NewEmpty(
            self.__code__.co_argcount - (1 if self.__code__.co_flags & 0x08 else 0),
            self.__code__.co_flags,
            self.__code__.co_stacksize)
f = func(func_obj_cover_fn)
assert inspect.getargspec(f) == getargspec(f)

import tokenize

assert getargspec.__doc__ == inspect.getargspec.__doc__
assert getargspec.__module__ == inspect.getargspec.__module__
if sys.version_info[:2] < (3, 3
