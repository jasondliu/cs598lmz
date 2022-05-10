from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(1)

# 上述代码等价于下面的代码
s = Struct('i')
s.pack(1)

# 如果需要在自定义类中使用_struct对象，那么可以通过下面的方式创建
class MyStruct(Struct):
    def __init__(self, *args, **kwargs):
        super(MyStruct, self).__init__(*args, **kwargs)

# 在Python中，类的实例化过程包含了__new__和__init__两个方法，__new__方法的返回值将作为__init__方法的第一个
