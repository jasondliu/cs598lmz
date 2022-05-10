from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda"))

# -*- coding: utf-8 -*-

# Вызов без аргументов
result = lambda: 'result'
print(result())

# Вызов с одним аргументом
result = lambda x: x
print(result(2))

# Вызов с двумя аргументами
result = lambda x, y: x + y
print(result(2, 3))

# Вызов с тремя аргументами
result = lambda x, y, z: x + y + z
print(result(2, 3, 4))

# Вызов с переменным числом аргу
