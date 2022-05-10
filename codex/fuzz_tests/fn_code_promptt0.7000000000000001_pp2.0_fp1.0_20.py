fn = lambda: None
# Test fn.__code__
print(getattr(fn, "__code__", None))
# Test fn.__closure__
print(getattr(fn, "__closure__", None))
# Test fn.__name__
print(getattr(fn, "__name__", None))

print(fn.__code__)
print(fn.__closure__)
print(fn.__name__)

def get_attributes(obj):
    return [i for i in dir(obj) if not i.startswith('__')]

print(get_attributes(fn))
print(get_attributes(fn.__code__))
print(get_attributes(fn.__closure__))
print(get_attributes(fn.__name__))

# Example 1:
def foo():
    def bar():
        # ...
        pass

print(foo.__code__.co_freevars) # ('bar',)
print(foo.__closure__) # None
print(foo.__closure__[0].cell_contents) # <function foo.<locals>.bar at
