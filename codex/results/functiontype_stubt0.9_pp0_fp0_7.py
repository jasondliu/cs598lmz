from types import FunctionType
a = (x for x in [1])
print(type(a))

# 生成器不可进行强制类型转换
# b = int(a)


"""
isinstance() 和 type() 区别：
  type()不会认为子类是一种父类类型，不考虑继承关系
  isinstance() 会认为子类是一种父类类型，考虑继承关系
"""
# 判断不支持文件操作，所以以模块的形式引入
# from file_and_except import myfile

class A():
    pass

class B(A):
    pass

isinstance(A
