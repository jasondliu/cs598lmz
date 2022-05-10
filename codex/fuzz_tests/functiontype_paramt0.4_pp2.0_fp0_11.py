from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo', (), None, None))
# [None]
</code>

