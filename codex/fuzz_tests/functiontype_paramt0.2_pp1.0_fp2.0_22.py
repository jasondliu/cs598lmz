from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo'))

# Test that the repr of a function is evalable
def f():
    pass

repr(f)

# Test that the repr of a builtin function is evalable
repr(len)

# Test that the repr of a builtin method is evalable
repr(str.upper)

# Test that the repr of a method is evalable
repr(str().upper)

# Test that the repr of a method is evalable
repr(str().upper)

# Test that the repr of a method is evalable
repr(str().upper)

# Test that the repr of a method is evalable
repr(str().upper)

# Test that the repr of a method is evalable
repr(str().upper)

# Test that the repr of a method is evalable
repr(str().upper)

# Test that the repr of a method is evalable
repr(str().upper)

# Test that the repr of a method is evalable
repr(str().upper)

# Test
