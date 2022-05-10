import weakref

class WeakMethod(object):
    def __init__(self, func):
        self.__func = weakref.ref(func.im_func)
        self.__self = weakref.ref(func.im_self)
        self.__class = func.im_class

    def __call__(self):
        func = self.__func()
        self_ = self.__self()
        if self_ is not None:
            return func.__get__(self_, self.__class)
        else:
            return None
