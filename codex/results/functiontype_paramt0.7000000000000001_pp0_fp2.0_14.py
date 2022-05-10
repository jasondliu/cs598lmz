from types import FunctionType
list(FunctionType().__dict__.keys())

# ['__module__', '__annotations__', '__name__', '__qualname__']

# не получилось посмотреть, какие методы определены в функции

# создаем декоратор, использующий обычные параметры и модифицирующий функцию в аргументе с помощью кода из метода __call__

class MyDecorator():
    def __init__(self, param1='
