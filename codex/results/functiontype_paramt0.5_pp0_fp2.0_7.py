from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda"))

# [<function <lambda> at 0x7f6c4d6d4f28>]

# >>> list(FunctionType(lambda x: x, globals(), "lambda"))[0]
# <function <lambda> at 0x7f6c4d6d4f28>

# >>> list(FunctionType(lambda x: x, globals(), "lambda"))[0](1)
# 1

# >>> FunctionType(lambda x: x, globals(), "lambda")()(1)
# 1

# >>> FunctionType(lambda x: x, globals(), "lambda")()(2)
# 2

# >>> FunctionType(lambda x: x, globals(), "lambda")()(3)
# 3

# >>> FunctionType(lambda x: x, globals(), "lambda")()(4)
# 4

# >>> FunctionType(lambda x: x, globals(), "lambda")()(5)
# 5

# >>> FunctionType(lambda x: x, globals(), "lambda")()(6)
