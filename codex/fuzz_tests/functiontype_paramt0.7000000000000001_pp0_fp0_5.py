from types import FunctionType
list(FunctionType(f.__code__, globals(), name="dummy").__globals__.keys())
</code>
output:
<code>['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names', '__all__', 'f', 'FunctionType']
</code>
As you can see, all of the builtin names are there. If you want to get rid of them, you can use a set difference:
<code>from types import FunctionType
from pprint import pprint

f = lambda: None

builtins = dir(__builtins__)
globals = list(FunctionType(f.__code__, globals(), name="dummy").__globals__.keys())
pprint(set(globals) - set(builtins))
</code>
output:
<code>{'__all__',
 '__annotations__',
 '__cached__',
 '__doc
