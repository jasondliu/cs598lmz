from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda').__code__.co_varnames)

list(FunctionType(lambda x: None, globals(), 'lambda').__code__.co_varnames)

list(FunctionType(lambda x, *args: None, globals(), 'lambda').__code__.co_varnames)

list(FunctionType(lambda x, y=1, *args, z=3, **kwargs: None, globals(), 'lambda').__code__.co_varnames)

list(FunctionType(lambda *args, z=3, **kwargs: None, globals(), 'lambda').__code__.co_varnames)

list(FunctionType(lambda x=1, **kwargs: None, globals(), 'lambda').__code__.co_varnames)

list(FunctionType(lambda x=1, y=2, **kwargs: None, globals(), 'lambda').__code__.co_varnames)

list(FunctionType(lambda x=1, y=2, *args, **kwargs: None
