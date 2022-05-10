from _struct import Struct
s = Struct.__new__(Struct)
s.size = 1
print(s.size)

# 打印s的类型
print(type(s))

# 打印s的父类
print(repr(s.__bases__))

# 打印s的对象类型
print(repr(s.__class__))

# 打印s的父类
print(repr(s.__base__))

# 打印s的属性
print(s.__dict__)

# 打印s的类型
print(type(type(int)))

# 打印s的父类
print(repr(type(int).__bases__))

# 打印s的对象类型
print(repr(type(int).__class__))

# 打印s的父
