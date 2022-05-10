fn = lambda: None
# Test fn.__code__ to produce a code object.
@constexpr
def fn():
    return 42

code = fn.__code__
assert type(code) is code
assert code.co_argcount == 1
assert code.__class__ == code
assert type(code.co_name) is str
assert code.co_filename == __file__
assert code.co_firstlineno == 4
assert code.co_lnotab is None

# Test fn.__code__ to pass a test.
assert code is fn.__code__
assert code.__class__ is code
assert code.co_name is fn.__name__


class X:
    @constexpr
    def method(self):
        return 42

x = X()
code = x.method.__code__
assert type(code) is code
assert code.co_argcount == 2
assert code.__class__ == code
assert type(code.co_name) is str
assert code.co_filename == __file__
assert code.co_firstlineno == 9
assert code.co_lnotab is None


