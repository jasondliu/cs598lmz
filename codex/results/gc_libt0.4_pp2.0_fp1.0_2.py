import gc, weakref, sys, traceback

class WeakMethod(object):
    """
    This class is a weakref.proxy for methods.
    """
    def __new__(cls, method):
        if isinstance(method, WeakMethod):
            return method
        else:
            return super(WeakMethod, cls).__new__(cls, method)

    def __init__(self, method):
        if isinstance(method, WeakMethod):
            return

        if isinstance(method, types.MethodType):
            self.__func = weakref.proxy(method.im_func)
            self.__self = weakref.proxy(method.im_self)
        elif isinstance(method, types.FunctionType):
            self.__func = weakref.proxy(method)
            self.__self = weakref.proxy(None)
        else:
            raise TypeError("Unsupported type for WeakMethod: %s" % type(method))

    def __call__(self, *args, **kwargs):
        if self.__self is None:
            return self.
