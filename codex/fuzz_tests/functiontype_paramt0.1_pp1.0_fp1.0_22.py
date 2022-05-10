from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(10))

# Test that we can create a function with a non-string name
list(FunctionType(lambda: None, globals(), b'foo') for _ in range(10))

# Test that we can create a function with a non-string name
list(FunctionType(lambda: None, globals(), u'foo') for _ in range(10))

# Test that we can create a function with a non-string name
list(FunctionType(lambda: None, globals(), bytearray(b'foo')) for _ in range(10))

# Test that we can create a function with a non-string name
list(FunctionType(lambda: None, globals(), memoryview(b'foo')) for _ in range(10))

# Test that we can create a function with a non-string name
list(FunctionType(lambda: None, globals(), memoryview(u'foo')) for _ in range(10))

# Test that we can create a function with a non-string name
list(FunctionType(lambda:
