from types import FunctionType
list(FunctionType(f.__code__, globals())(*a))

#[1, 2, 3, 4]
</code>

