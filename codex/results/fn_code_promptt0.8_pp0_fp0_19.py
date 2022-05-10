fn = lambda: None
# Test fn.__code__
# Test fn.__call__
# Test fn.__dict__
# Test fn.__module__
# Test fn.__defaults__
# Test fn.__kwdefaults__
# Test fn.__annotations__

# Test fn.__closure__
def make():
    x = 10
    def inner():
        return x
    return inner

fn = make()
# Test fn.__closure__

# Test classes
class A:
    # Test A.__bases__
    # Test A.__name__
    # Test A.__mro__
    # Test A.__dict__
    # Test A.__module__
    # Test A.__doc__
    # Test A.__annotations__
    # Test A.__call__
    # Test A.__qualname__
    # Test A.__subclasses__
    x = 10
    def a(self):
        return self.x
    # Test A.a.__module__
    # Test A.a.__qualname__
    # Test A.a.__code__
   
