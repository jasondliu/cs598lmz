from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 使用__new__方法，可以在__init__之前对类进行初始化

# __new__方法的第一个参数是cls，它代表要实例化的类，此参数在实例化时由Python解释器自动提供(例如下文的User和Supplier)。
# 并且调用__new__方法的还是类，而不是实例。
# __new__方法的第二个参数是类的名字，比如User继承自Model，它的
