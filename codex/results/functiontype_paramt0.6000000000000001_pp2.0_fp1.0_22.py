from types import FunctionType
list(FunctionType(list(FunctionType.__dict__.values()), globals())())
</code>

