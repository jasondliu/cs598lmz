from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<i")
print(s.size)

# 使用__new__方法创建一个类的实例，并返回该实例
# 使用__init__方法初始化类的实例

# 如果一个类定义了__new__方法，那么它的实例化操作会调用__new__方法
# 如果一个类没有定义__new__方法，那么它的实例化操作会调用其基类的__new__方法
# 如果一个类没有定义__init__方法
