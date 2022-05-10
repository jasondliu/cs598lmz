from types import FunctionType
list(FunctionType(lambda a: a, globals(), 'lambda') for a in [])
