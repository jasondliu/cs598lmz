from types import FunctionType
list(FunctionType(lambda:None,globals(),'lambda').__code__.co_varnames)

# 从函数的全局命名空间里，获取全局变量的名字
globals().keys()

# 从函数的局部命名空间里，获取局部变量的名字
locals().keys()

# 从函数的局部命名空间里，获取局部变量的名字
locals().keys()

# 从函数的局部命名空间里，获取局部变量的名字
locals().keys()

# 从函数的
