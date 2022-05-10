from types import FunctionType
list(FunctionType(add.__code__, {}, 'add').__globals__.keys())

# 全局变量
# 全局变量是定义在模块里且在函数体之外的变量
# 全局变量可以被函数体中的所有代码引用(包括函数体内的函数)
# 可以通过global关键字来修改全局变量的值

# 局部变量
# 局部变量是函数体内的变量，函数体外的代码不能引用局部变量
# 局部变量
