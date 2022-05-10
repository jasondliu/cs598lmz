from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 创建一个空的类
class MyEmptyClass:
    pass

# 创建一个类，并且指定父类
class MySubClass(MyEmptyClass):
    pass

# 创建一个类，并且指定多个父类
class MySubClass(MyEmptyClass, MyOtherClass):
    pass

# 创建一个类，并且指定多个父类，并且指定父类的搜索顺序
class MySubClass(MyOtherClass, MyEmptyClass):
    pass

# 创建一个类，并且指定多
