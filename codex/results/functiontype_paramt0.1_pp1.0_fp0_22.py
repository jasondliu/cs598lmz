from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that we can create a function with a non-string name
# (see issue #16056)
list(FunctionType(lambda: None, globals(), b'foo'))

# Test that we can create a function with a non-string name
# (see issue #16056)
list(FunctionType(lambda: None, globals(), bytearray(b'foo')))

# Test that we can create a function with a non-string name
# (see issue #16056)
list(FunctionType(lambda: None, globals(), memoryview(b'foo')))

# Test that we can create a function with a non-string name
# (see issue #16056)
list(FunctionType(lambda: None, globals(), 'foo'.encode('utf-8')))

# Test that we can create a function with a non-string name
# (see issue #16056)
list(FunctionType(lambda: None, globals(), 'foo'.encode('utf-16')))

# Test
