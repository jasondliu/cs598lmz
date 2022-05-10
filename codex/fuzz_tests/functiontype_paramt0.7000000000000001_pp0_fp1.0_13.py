from types import FunctionType
list(FunctionType(f.__code__,globals(),name=f.__name__)() for f in [lambda:i for i in range(10)])
</code>

