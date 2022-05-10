from types import FunctionType
list(FunctionType(func).__code__.co_varnames)

# или просто
def func():
    a = 1
    b = 2
    return a + b
func.__code__.co_varnames

# но не работает со строками
def func():
    a = 1
    b = 2
    return a + b

func.__code__.co_code

# поэтому надо передавать в виде функции
import dis
dis.dis(func)

# запомнить точку вызова
def func():
    a = 1
    b = 2
    return a + b

import inspect
inspect.stack()

# теперь можно доб
