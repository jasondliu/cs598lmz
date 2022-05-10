from types import FunctionType
list(FunctionType(f2.func_code, globals(), "f2")) # works
</code>
If you want to keep the original function name (e.g. for logging) you can use a decorator:
<code>import inspect
def lowercased(f):
    def _(*args, **kwargs):
        return f(*args, **kwargs)
    return FunctionType(f.func_code, globals(), inspect.getmodule(f).__name__,
                        inspect.getargspec(f))

lowercased(f2)() # works
</code>

