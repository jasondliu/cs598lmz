import types
# Test types.FunctionType
def func1():
    pass
print(type(func1))

# Test types.LambdaType
# 匿名函数
# lambda 函数只能有一个表达式，不用写return，返回值就是该表达式的结果。
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
# 当lambda只有一个参数时，可以省略它的括号。
# 当lambda函数有多个参数时，它们之间需
