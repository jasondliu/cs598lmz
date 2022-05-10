from _struct import Struct
s = Struct.__new__(Struct)
print(s)
print(type(s))
print(s.format)
print(s.size)
# 方法
# s.unpack()
# s.pack()


# _struct.Struct.__new__
# _struct.Struct.unpack
# _struct.Struct.pack

# class。__new__
# class。__init__
# class.方法

# class.__new__
# class.__init__
# class.方法


# 创建一个类
# class A(object, metaclass=type):
#     def __init__(self):
#         print('__init__')
#
#     def __new__(cls):
#         print('__new__')
#         return object.__new__(cls)
#
#     def run(self):
#         print('run')
#
#
# a = A()   # __new__  __init__
# a.run()   # run



# 创建
