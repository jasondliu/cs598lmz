from types import FunctionType
list(FunctionType(f.func_code, f.func_globals))

# or an even simpler way:
list(f.im_func)

# except that the latter doesn't work if you have an instancemethod
f = foo()
list(f.im_func)  # AttributeError: im_func
</code>

