from types import FunctionType
list(FunctionType(lambda x: x, {}, 'lambda', (lambda: None).__code__, None))

# [1, 2, 3]
[1,2,3]

# {'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'b': 2, 'c': 3}
