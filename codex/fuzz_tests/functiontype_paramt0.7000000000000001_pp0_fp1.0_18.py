from types import FunctionType
list(FunctionType(x, globals(), 'x') for x in (lambda: 'hello',
                                               lambda: 'world'))

# This can be used as a decorator
class inspect(object):
    def __init__(self, f):
        self.f = f
        # self.__doc__ = f.__doc__
        # self.__name__ = f.__name__

    def __call__(self, *args, **kwargs):
        print 'call', args, kwargs
        return self.f(*args, **kwargs)

@inspect
def func(a, b, c=1):
    print a, b, c

func(2, 3, 4)
# call (2, 3, 4) {}
# 2 3 4

# Moreover, we can use this pattern to make a "callable" object that
# can be called later in the program:
class PrintCall(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print '
