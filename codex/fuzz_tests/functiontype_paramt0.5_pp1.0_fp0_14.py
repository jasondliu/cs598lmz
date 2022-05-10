from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__) # ['__builtins__']
</code>

