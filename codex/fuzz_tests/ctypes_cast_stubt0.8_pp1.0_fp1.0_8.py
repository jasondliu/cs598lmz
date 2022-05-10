import ctypes
ctypes.cast(id(int), ctypes.py_object).value

def func():
    return int  # this is the pointer we need in Python 3

func.__closure__[0].cell_contents

ctypes.cast(id(func), ctypes.py_object).value

sys.getrefcount(func)

ctypes.cast(id(func), ctypes.py_object).value

ctypes.cast(id(int), ctypes.py_object).value

import inspect

inspect.getsourcefile(int)

inspect.getsource(int)

inspect.getfile(int)

inspect.getsourcefile(func)

inspect.getsource(func)

inspect.getfile(func)

dir(func)

func.__closure__

func.__code__

func.__defaults__

func.__annotations__

func.__globals__

func.__closure__[0]

func.__closure__[0].cell_contents is int

func.__
