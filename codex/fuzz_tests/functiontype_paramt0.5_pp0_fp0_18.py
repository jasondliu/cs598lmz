from types import FunctionType
list(FunctionType(FunctionType.__code__, globals(), 'func'))()

# TypeError: list() takes no arguments (1 given)
</code>
И вот тут я не понимаю, как мне передать аргументы в функцию. Подскажите, пожалуйста, как это можно сделать.
Пробовал вот так:
<code>from types import FunctionType
FunctionType(FunctionType.__code__, globals(), 'func')('foo', 'bar')

# TypeError: list() takes no arguments (2 given)
</code>
Выдаёт такую же ошибку.


A
