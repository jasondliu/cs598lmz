fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16283: Ensure that the __code__ attribute of built-in functions
# is a code object, not a function.
import types
assert isinstance(types.__dict__['FunctionType'].__code__, types.CodeType)

# Issue #16284: Ensure that the __code__ attribute of built-in methods
# is a code object, not a function.
assert isinstance(types.__dict__['MethodType'].__code__, types.CodeType)

# Issue #16285: Ensure that the __code__ attribute of built-in classes
# is a code object, not a function.
assert isinstance(types.__dict__['ClassType'].__code__, types.CodeType)

# Issue #16286: Ensure that the __code__ attribute of built-in type objects
# is a code object, not a function.
assert isinstance(type(object).__code__, types.CodeType)

# Issue #16287: Ensure that the __code__ attribute of built-in exceptions
# is a code object, not a function.

