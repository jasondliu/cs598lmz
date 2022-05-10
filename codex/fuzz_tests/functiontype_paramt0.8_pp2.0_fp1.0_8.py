from types import FunctionType
list(FunctionType(x,globals(), 'foo')() for x in (y.__code__ for y in bar))
</code>

