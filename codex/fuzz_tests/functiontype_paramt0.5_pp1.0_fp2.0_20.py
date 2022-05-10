from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# 使用内置的vars函数
vars(FunctionType(lambda: None, {}))

# 使用内置的locals函数
locals()

# 使用内置的globals函数
globals()
