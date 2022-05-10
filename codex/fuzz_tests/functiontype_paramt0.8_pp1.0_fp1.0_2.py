from types import FunctionType
list(FunctionType(f.code, f.globals, 'foo').__globals__.keys())
# ['list', '__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', 'FunctionType']
</code>

