fn = lambda: None
# Test fn.__code__ and fn.__code__.co_lnotab.
code = fn.__code__
assert type(code) is _types.CodeType
# 'co_lnotab' is the mapping between bytecode offsets and source line numbers.
# For the test function, there are no line mappings, so co_lnotab == b''.
assert code.co_lnotab is b''

# Test code.signature()
assert str(code.signature) == "(): NoneType"

# Test code.co_flags
assert code.co_flags == 67


# Test co_flags.flag names.
cf = code.co_flags
NAMES = {"OPTIMIZED", "NEWLOCALS", "VARARGS", "VARKEYWORDS", "NESTED",
         "GENERATOR", "NOFREE", "COROUTINE", "ITERABLE_COROUTINE",
         "ASYNC_GENERATOR"}
for name in NAMES:
    assert hasattr(cf, name)


# Test marshaling code object
# First, write the code object to a file
