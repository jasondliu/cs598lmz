from types import FunctionType
a = (x for x in [1])
b = [1]
m = b.__iter__()
print(type(a))
print(type(m))  # 迭代器也是动态性挣挣着,迭代器也是可迭代对象
d = {}
print(type(d.__missing__))
print(type(int.__missing__))
# print(type(FunctionType.__missing__))
# print(int.__missing__)  # ?
print(a.__missing__)  # ?   迭代器有了这部分,也增加了自己开辟空间,存储函数,说明迭代器也是动态性饿挣扎着
"""


"""
print("*"*40)
import builtins
print(builtins.__dict__["__missing__"])
