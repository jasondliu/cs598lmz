from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<i'
s.size = 4
s.pack(1)

# 使用__new__方法创建类的实例时，若没有指定父类，则默认继承自object
# 若指定父类，则父类必须是type类的实例
# 创建类的实例时，若没有指定父类，则默认继承自object
# 若指定父类，则父类必须是type类的实例
# 创建类的实
