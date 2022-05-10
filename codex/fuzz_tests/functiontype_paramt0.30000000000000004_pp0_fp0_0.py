from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# FunctionType(code, globals[, name[, argdefs[, closure]]])
# 创建一个函数对象，code是一个code对象，globals是函数的全局符号表，name是函数的名字，argdefs是参数的默认值，closure是函数的闭包

# lambda x: x
# 创建一个匿名函数，x是参数，x: x是函数体

# globals()
# 返回当前位置的全局符号表

# 'lambda'
# 函数名字

# 创建一个
