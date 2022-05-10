from types import FunctionType
list(FunctionType(lambda x: x, {}).__globals__.keys()) 
['list', 'FunctionType', 'dict', '__builtins__']
</code>

