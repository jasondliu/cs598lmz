from types import FunctionType
list(FunctionType(lambda:0,globals()) for i in range(10))

#The above is equivalent to:
def f(): return 0
list(FunctionType(f.__code__,globals()) for i in range(10))
</code>

