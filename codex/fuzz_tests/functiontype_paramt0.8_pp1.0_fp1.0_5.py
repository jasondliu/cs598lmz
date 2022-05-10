from types import FunctionType
list(FunctionType(f.__code__,{},name=f.__name__).__globals__.keys())
</code>
Which, for the module above, returns:
<code>['module_name', 'module_variable', '__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__']
</code>

