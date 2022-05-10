from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# __new__方法的第一个参数是cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
# 并且从类的定义中获得

# 实例化时调用__init__方法，为类加上数据属性，初始化对象
# 如果没有定义__init__方法，就只有类的数据属性了，没有实例变量

# 注意
