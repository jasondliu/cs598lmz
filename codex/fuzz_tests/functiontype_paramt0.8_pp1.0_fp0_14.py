from types import FunctionType
list(FunctionType(repr).__dict__)

# Определение всех атрибутов функции
def func(x: int) -> str:
    pass
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)
print(func.__code__.co_argcount)
print(func.__code__.co_consts)
print(func.__code__.co_cellvars)
print(func.__code__.co_freevars)
print(func.__code__.co_stacksize)
print(func.__code__.co_filename)
print(func.__code__.co_name)
print(func.__code__.co_names)
print(func.__code__.co_nlocals)
print(func.__code__.co_firstlineno)
print(func.__code__.co_lnotab)
print(f
