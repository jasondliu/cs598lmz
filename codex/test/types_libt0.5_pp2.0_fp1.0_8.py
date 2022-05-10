import types
types.FunctionType

#把函数赋值给变量，通过变量来调用函数
a = abs # 变量a指向abs函数
a(-1) # 所以也可以通过a调用abs函数

#函数名也是变量
abs = 10
abs(-10)
