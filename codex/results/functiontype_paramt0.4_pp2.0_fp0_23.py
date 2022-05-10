from types import FunctionType
list(FunctionType(f.__code__, globals(), name="f") for f in (f1, f2, f3))
</code>

