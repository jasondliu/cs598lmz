from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__builtins__', '__name__', '__doc__', '__package__']

# This is the same as the builtin function `dir`
# except that it doesn't return the special attributes
# that are set by the interpreter.

def dir2(obj):
    return [name for name in dir(obj)
            if not name.startswith('__')]

dir2(5)

# ['bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# The builtin function `dir` is implemented in C,
# so it's faster than the above Python implementation.

# The builtin function `dir` is implemented in C,
# so it's faster than the above Python implementation.

# The builtin function `dir` is implemented in C,
# so it's faster than the above Python implementation.

# The builtin function `dir` is implemented in C,
# so it's
