from types import FunctionType
list(FunctionType(lambda x:x, {}).__globals__.keys())[0]

dir(FunctionType(lambda x:x, {}))
help(FunctionType(lambda x:x, {}))
