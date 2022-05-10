import types
types.MethodType(func, None, type)

# 先定义函数，然后把函数赋值给一个变量，通过该变量来调用这个函数
a = abs # 变量a指向abs函数
a(-1) # 此时，通过a调用abs函数

# 使用type()函数可以查看对象的类型，比如str、list、tuple、dict
type(a)

# 变量a现在已经指向abs函数本身，并不是指向abs这个函数返回的函数地址
