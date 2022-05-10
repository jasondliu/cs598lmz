from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda"))

# list(FunctionType(lambda x: x, globals(), "lambda"))
# [<function <lambda> at 0x7f3d9e9d3d08>]

# list(FunctionType(lambda x: x, globals(), "lambda"))[0]
# <function <lambda> at 0x7f3d9e9d3d08>

# list(FunctionType(lambda x: x, globals(), "lambda"))[0](1)
# 1

# list(FunctionType(lambda x: x, globals(), "lambda"))[0](2)
# 2

# list(FunctionType(lambda x: x, globals(), "lambda"))[0](3)
# 3

# list(FunctionType(lambda x: x, globals(), "lambda"))[0](4)
# 4

# list(FunctionType(lambda x: x, globals(), "lambda"))[0](5)
# 5

# list(FunctionType(lambda x: x, globals(), "lambda"))[0](6
