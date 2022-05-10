from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, None, None, f.__closure__)
         for f in (lambda: lambda: 42, lambda: None))
# [<function <lambda>>, <function <lambda>>]

# Not supported:
# lambda: (lambda: 42)()
# lambda: lambda x: lambda y: 42

# TODO: lambdas with statements

# TODO: proper function-level locals

# TODO: support for for-else and try-except-else-finally

# TODO: support for annotations

# TODO: support for type comments

# TODO: add backticks to the parser

# TODO: support for the return type of the __annotations__ attribute

# TODO: support for the __slots__ attribute
