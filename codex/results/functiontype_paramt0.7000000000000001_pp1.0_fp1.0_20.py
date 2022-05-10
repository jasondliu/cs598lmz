from types import FunctionType
list(FunctionType(pickle.loads(d), globals(), 'f')())

# [1, 2, 3]

# Note that the last argument to FunctionType is the name of the function.
# This is only used for reporting in tracebacks and for the repr of the function.
#
# You can also use it as follows:
#
# >>> FunctionType(c, globals())()
# [1, 2, 3]
# >>>
#
# but then the function will have no __name__ and the repr will show <lambda>.
#
# If you want to create a function from source code, you can use the compile built-in and the exec statement:
#
# >>> exec(compile('def f(): return [1, 2, 3]', '', 'single'))
# >>> f()
# [1, 2, 3]
# >>>
#
# or use the compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1) function,
# if you don't want the function to have the __name__ and __qualname__ of the 'f' name.

