from types import FunctionType
list(FunctionType(x, globals(), '_')())

# def f(x):
#     return eval(compile(x, '', 'exec'))
