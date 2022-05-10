fn = lambda: None
# Test fn.__code__.co_varnames
setattr(fn, '__code__', code)
print(fn.__code__.co_varnames)

# Test: 'code' as an instance variable has the same effect
class Test:
    def __init__(self):
        self.code = code
        self.func = lambda self: None

t = Test()
print(t.func.__code__.co_varnames)
