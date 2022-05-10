from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, 'f', f.func_defaults, f.func_closure) for f in (lambda: (yield i) for i in range(10)))
</code>

