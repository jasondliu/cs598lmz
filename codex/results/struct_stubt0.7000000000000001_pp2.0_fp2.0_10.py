from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('7s 2s f')
s.size

# ###############
# 修改元类
# 如果要继承type来创建自定义元类，需要实现__new__方法
# 元类只能定义在使用它来创建类型的模块中，而不是在类定义体中。


# ###############
# 编码解码对象
# 使用dumps和loads编码和解码对象

class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass({
