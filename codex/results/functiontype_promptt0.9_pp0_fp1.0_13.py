import types
# Test types.FunctionType when frame introspection is enabled and test
# that it works even when the function doesn't have __globals__
# attribute or co_globals.

def foo():
    pass

print(types.FunctionType is type(foo))
print(isinstance(foo, types.FunctionType))

def bar():
    pass
bar.__globals__ = None
bar.__code__.co_globals = None

class A:
    def __getattr__(self, attr):
        print(attr)
        return None

print(types.FunctionType is type(bar))
print(isinstance(bar, types.FunctionType))

# Make sure that FunctionType has a __dict__
print(hasattr(types.FunctionType, "__dict__"))
