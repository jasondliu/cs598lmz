fn = lambda: None
# Test fn.__code__.co_name
# Test fn.__closure__
# Test fn.__defaults__
# Test fn.__globals__
# Test fn.__kwdefaults__
# Test fn.__module__
# Test fn.__name__
# Test fn.__dict__


class A:
    def meth(self):
        pass

# Test A.__dict__
# Test A.__doc__
# Test A.__module__

# Test A.meth.__annotations__
# Test A.meth.__closure__
# Test A.meth.__code__
# Test A.meth.__defaults__
# Test A.meth.__get__
# Test A.meth.__globals__
# Test A.meth.__kwdefaults__
# Test A.meth.__code__.co_name
# Test A.meth.__name__
# Test A.meth.__self__
# Test A.meth.__dict__

# Test classobj.__bases__
# Test classobj.__
