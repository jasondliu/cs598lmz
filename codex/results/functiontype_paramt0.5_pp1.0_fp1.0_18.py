from types import FunctionType
list(FunctionType(s,globals(),'foo')())

# There are also a couple of other ways to create functions, but they are
# not as useful as the functional tools.

# The first is to call a function and assign it to a variable.  This is
# useful for functions that are defined elsewhere.

def foo(): print 'foo'
f = foo
del foo
f()

# The second way is to use the type constructor.  This is not useful
# because it has no way to specify the code of the function.

# FunctionType(code,globals[,name[,argdefs[,closure]]])
# FunctionType(code,globals[,argdefs[,closure]])
FunctionType(f.func_code,f.func_globals,f.func_name,f.func_defaults,f.func_closure)

# The function type constructor is the only way to create functions with
# closures, but this is not very useful because the closure is not
# specified by a tuple of cell objects.

def foo(x):
    def bar():
       
