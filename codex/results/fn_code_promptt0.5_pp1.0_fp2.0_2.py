fn = lambda: None
# Test fn.__code__.co_varnames
# Test fn.__code__.co_argcount

class C:
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return self.s

# Test keyword arguments
# Test kwargs
# Test kwargs.keys()
# Test kwargs.values()
# Test kwargs.items()

# Test isinstance
# Test issubclass

# Test isinstance(x, type)
# Test issubclass(x, type)
# Test issubclass(type, x)
# Test issubclass(type, type)

# Test isinstance(x, type(x))
# Test issubclass(type(x), x)
# Test issubclass(x, type(x))

# Test isinstance(x, type(y))
# Test issubclass(type(y), x)
# Test issubclass(x, type(y))

# Test isinstance(x, type(None))
# Test issubclass(type(None),
