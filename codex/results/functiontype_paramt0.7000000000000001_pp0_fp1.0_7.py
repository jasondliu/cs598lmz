from types import FunctionType
list(FunctionType(x,globals()) for x in (lambda:0,lambda:0))
</code>
Why?

