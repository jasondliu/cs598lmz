gi = (i for i in ())
# Test gi.gi_code:
FunctionCodeType = type(gi.gi_code)
assert type(gi.gi_code) is FunctionCodeType
assert isinstance(gi.gi_code, FunctionCodeType)
# Test gi.__code__:
CodeType = type(gi.__code__)
assert type(gi.__code__) is CodeType
assert isinstance(gi.__code__, CodeType)

def f():
    def g():
        pass
    return g
# Test f.__code__.co_name:
co = f.__code__
co2 = f().__code__
assert 'f' == co.co_name
assert 'g' == co2.co_name
# Test f.gi_code.co_name:
co = f.gi_code
co2 = f().gi_code
assert 'f' == co.co_name
assert 'g' == co2.co_name

# Test is_in_test_build()

assert is_in_test_build() is False

# Test assertRaises()

assertRaises(Attribute
