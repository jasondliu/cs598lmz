import types
types.FunctionType

#把函数赋值给变量，通过变量来调用函数
a = abs # 变量a指向abs函数
a(-1) # 所以也可以通过a调用abs函数

#函数名也是变量
abs = 10
abs(-10)

#传入函数
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def add(x, y, f):
    return f(x) + f(y)

add(-5, 6, abs)

#map/reduce
#map()函数
