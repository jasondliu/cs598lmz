from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))
list(FunctionType(lambda: None, globals(), 'foo', (1, 2, 3)))
list(FunctionType(lambda: None, globals(), 'foo', (1, 2, 3), {'a': 1}))
list(FunctionType(lambda: None, globals(), 'foo', (1, 2, 3), {'a': 1}, True))
list(FunctionType(lambda: None, globals(), 'foo', (1, 2, 3), {'a': 1}, True, True))
list(FunctionType(lambda: None, globals(), 'foo', (1, 2, 3), {'a': 1}, True, True, True))
list(FunctionType(lambda: None, globals(), 'foo', (1, 2, 3), {'a': 1}, True, True, True, True))
list(FunctionType(lambda: None, globals(), 'foo', (1, 2, 3), {'a': 1}, True, True, True, True, True))
list(FunctionType(lambda: None, globals(), 'foo',
