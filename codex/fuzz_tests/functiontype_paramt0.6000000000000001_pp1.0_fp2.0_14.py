from types import FunctionType
list(FunctionType(x) for x in [1, 2, 3])
</code>
The compiler doesn't complain about this, but it should.

