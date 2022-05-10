from types import FunctionType
a = (x for x in [1])
print(isinstance(a,FunctionType))

# 全局变量和局部变量
# a = 100
# b = 1000
# def fun1():
#     a = 200
#     print(a)
#     # print(b)
# fun1()
# print(a)

# 访问函数内部变量
# def fun2():
#     a = 100
#     print(locals())
# fun2()

# 全局变量
# a = 100
# def fun3():
#     print(globals())
# fun3()

# 全局变量和局部变量
# a = 100
# b = 1000
# def fun4():
#     a = 200
#     print(a)
#     print(locals())
#     print(globals()["a"])
# fun4()
# print(a)


