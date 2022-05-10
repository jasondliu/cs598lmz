from types import FunctionType
list(FunctionType(lambda x: x+1,globals())(i) for i in range(5))

#------------------------------------------------------------
# получение списка параметров со значениями по умолчанию

def foo(bar, baz=3, zoo='qwerty'):
    return bar + baz + len(zoo)
foo(1)
foo(1,2)
foo(1,2,'asd')
foo(1,zoo='asd')
# в питоне 3 позиционные аргументы расположены перед именованными
foo(zoo='asd',baz=123,bar=1)

def foo_kwargs(**kwargs):
    return k
