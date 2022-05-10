from types import FunctionType
list(FunctionType(lambda: None, globals())().__closure__)
</code>

