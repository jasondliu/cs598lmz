from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# _struct.Struct.__new__()
# _struct.Struct.__init__()
# _struct.Struct.format
# _struct.Struct.size
# _struct.Struct.calcsize()

# 使用__new__()方法创建实例时，__init__()方法不会自动调用，需要自己调用
# 创建实例时，若__new__()方法中没有返回当前类的实例，则不会调用__init__()方法

# 利用__new__()方法实现单例模式
