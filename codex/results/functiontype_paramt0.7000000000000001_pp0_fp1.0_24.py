from types import FunctionType
list(FunctionType('a').__code__.co_varnames)

def get_varnames(func):
    return func.__code__.co_varnames

get_varnames(FunctionType('a'))
def get_varnames(func):
    return inspect.getclosurevars(func).nonlocals

get_varnames(FunctionType('a'))
type(FunctionType('a'))
_ = 10
type(FunctionType('a'))
get_varnames(FunctionType('a'))
get_varnames(FunctionType('a'))['_']
type(FunctionType('a'))
type(FunctionType('a'))
get_varnames(FunctionType('a'))
FunctionType('a')(_)
get_varnames(FunctionType('a'))
def get_varnames(func):
    if isinstance(func, FunctionType):
        return inspect.getclosurevars(func).nonlocals
    else:
        return func.__code__.co_varnames

get_varnames
