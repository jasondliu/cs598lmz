from types import FunctionType
list(FunctionType(x, globals(), 'f'))
list(FunctionType.__new__(FunctionType, x, globals(), 'f'))
list(eval('lambda: 1'))
list(eval('lambda: 1', globals(), {}))
list(eval('lambda: 1', globals(), {'__name__':'f'}))
list(eval('lambda: 1', globals(), {'__qualname__':'f'}))
