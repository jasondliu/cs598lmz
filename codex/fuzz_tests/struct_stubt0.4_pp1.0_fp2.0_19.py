from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)

#__new__方法的返回值将会被赋值给类变量__init__方法的第一个参数，
# 并且调用__init__方法。
# 所以，在__new__方法中创建的实例，必须由__new__方法返回，否则不会调用__init__方法。
#
# 如果__new__方法没有返回值，那么就不会调用__init__方法。
#
# 如果__new__方法返回的不是当前类的实例
