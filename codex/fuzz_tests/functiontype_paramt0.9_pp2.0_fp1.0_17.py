from types import FunctionType
list(FunctionType(int))
#> [<class 'int'>]
list(FunctionType(lambda: None))
#> [None, type(None)]
list(Functio
