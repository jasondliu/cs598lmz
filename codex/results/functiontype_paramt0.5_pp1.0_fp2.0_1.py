from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'add')(2))

import types
list(types.FunctionType(lambda x: x + 1, globals(), 'add')(2))
