from types import FunctionType
list(FunctionType(b.__code__, globals())(), FunctionType(b.__code__, globals())())
#[1, 2]
#[1, 2]
#[Finished in 0.1s]
</code>

