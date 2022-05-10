from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(1))
# [<function foo at 0x7f7c6d4f6b70>]

# create a function object from the code object
FunctionType(lambda: None.func_code, globals(), 'foo')
# <function foo at 0x7f7c6d4f6b70>

# create a function object from the code object and the globals
FunctionType(lambda: None.func_code, {}, 'foo')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'None' is not defined


# create a function object from the code object and the globals
FunctionType(lambda: None.func_code, {'None': None}, 'foo')
# <function foo at 0x7f7c6d4f6b70>

# create a function object from the code object and the globals
FunctionType(lambda: None.func_code, {'None': None}, 'foo', (), ('keyword_only
