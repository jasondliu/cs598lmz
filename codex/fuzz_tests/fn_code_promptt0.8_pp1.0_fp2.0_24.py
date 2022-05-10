fn = lambda: None
# Test fn.__code__.co_argcount

class Test(argcountTestClass):
    def __call__(self, *args):
        self.args = args

Test(1, 2, 3)
a = Test(1, 2, 3)
a.__init__(1, 2, 3)
a(1, 2, 3)

def simple_decorator(decorator):
    def new_decorator(f):
        g = decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g
    # Now a few lines needed to make simple_decorator itself
    # be a well-behaved decorator.
    new_decorator.__name__ = decorator.__name__
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)
    return new_decorator

@simple_
