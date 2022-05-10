from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# [<function <lambda> at 0x7f9b0c0c6d08>, <function <lambda> at 0x7f9b0c0c6d90>]

# В примере выше мы получили две функции, которые возвращают переданный им аргумент.
# Первая функция была создана в глобальной области видимости, а вторая в локальной.
# В обоих случая
