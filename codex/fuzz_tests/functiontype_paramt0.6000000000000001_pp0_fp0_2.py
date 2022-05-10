from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_varnames)

# Function annotations
def foo(x:int, y:str) -> str:
    return y*x
foo.__annotations__
# {'x': <class 'int'>, 'y': <class 'str'>, 'return': <class 'str'>}

# Function attributes
def foo(x, y, z=3, *args, **kwargs):
    return bar(x, y, z, *args, **kwargs)
foo.__defaults__ # (3,)
foo.__kwdefaults__ # {'z': 3}
foo.__code__.co_varnames  # ('x', 'y', 'z', 'args', 'kwargs')
foo.__code__.co_argcount  # 3
foo.__code__.co_nlocals  # 5
foo.__code__.co_stacksize  # 7
foo.__code__.co_flags  # 67
foo.__code__.co_code # b'd\x00\x17d
