from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), "foo")(3))

#
# The following is the same as above, but the function is created with a
# different syntax, and the call is made with a different syntax
#
def foo(x):
    return x + 1
list(foo(3))

#
# The following is the same as above, but the function is created with a
# different syntax, and the call is made with a different syntax
#
def foo(x):
    return x + 1
list(foo.__call__(3))

#
# The following is the same as above, but the function is created with a
# different syntax, and the call is made with a different syntax
#
def foo(x):
    return x + 1
list(foo.__call__.__call__(foo, 3))

#
# The following is the same as above, but the function is created with a
# different syntax, and the call is made with a different syntax
#
def foo(x):
    return x + 1
list(foo.__call__.__call__
