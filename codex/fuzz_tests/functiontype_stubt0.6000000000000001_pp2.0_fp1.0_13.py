from types import FunctionType
a = (x for x in [1])
print(type(a))

b = FunctionType(a.gi_frame.f_code, a.gi_frame.f_globals, a.gi_frame.f_name, a.gi_frame.f_locals)
print(b())

# 匿名函数
# 匿名函数 lambda x: x+1
# 匿名函数只能有一个表达式，不用写return，返回值就是该表达式的结果
# 匿名函数只能有一个参数
# 匿名函数的参数名是固定的，必须是x，不能是其他名字
# 举例
# def func(x):
#     return x+1
#
#
