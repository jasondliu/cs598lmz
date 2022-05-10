from types import FunctionType
list(FunctionType(f.func_code, {}).func_globals.keys())

# The above code is equivalent to:
# list(f.func_globals.keys())
</code>
For <code>f</code>, this yields <code>['__builtins__', 'sys', '__name__', '__doc__']</code>.

