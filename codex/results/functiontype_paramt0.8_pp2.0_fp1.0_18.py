from types import FunctionType
list(FunctionType('return 1', {}, 'a', ('b', 1), 1))
list(FunctionType('return 1', {}, 'a', ('b', 1), 1, 1, 'a'))
list(FunctionType('return 1', {}, 'a', ('b', 1), 1, 1, 'a', 'b'))
list(FunctionType('return 1', {}, 'a', ('b', 1), 1, 1, 'a', 'b', 'c'))
try:
    list(FunctionType())
except TypeError:
    print('TypeError')
try:
    list(FunctionType('return 1'))
except TypeError:
    print('TypeError')
try:
    list(FunctionType('return 1', {}))
except TypeError:
    print('TypeError')
try:
    list(FunctionType('return 1', {}, 'a'))
except TypeError:
    print('TypeError')
try:
    list(FunctionType('return 1', {}, 'a', ('b', 1)))
except TypeError:
    print('TypeError')
try:
    list(FunctionType
