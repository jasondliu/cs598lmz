import types
types.FunctionType(func)

# 返回函数的参数个数，即在函数定义中的位置参数个数
func.__code__.co_argcount

# 返回函数的所有局部变量名
func.__code__.co_varnames

# 返回函数的所有常量
func.__code__.co_consts

# 返回函数的所有全局变量名
func.__code__.co_names

# 返回函数的所有局部变量名（包括没有被赋值的变量）
func.__code__.co_varnames

# 返回
