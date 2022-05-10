from types import FunctionType
list(FunctionType(FunctionType.__code__, globals(), 'test')())
</code>
This works because the <code>__code__</code> attribute is a code object which can be used to create a new function.

