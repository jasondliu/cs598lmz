from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 8
print(s)
# <_struct.Struct object at 0x7f8b3c1745f0>

# 如果对象没有指定__format__方法，那么会使用__str__方法返回的值，
# 如果没有__str__方法那么会使用__repr__方法返回的值。

# 简单总结，__str__方法站在用户的角度，让用户知道对象的意思，
# __repr__方法站在开发者的角度，让开发者知道对象的细
