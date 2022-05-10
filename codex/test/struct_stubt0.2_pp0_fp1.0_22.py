from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.size

# 可以看到，Struct对象的size属性是可以被访问的，但是我们并不能直接访问Struct对象的__new__和__init__方法，这是因为它们是私有方法，只能在Struct内部访问。
# 如果我们要访问这些方法，可以使用特殊方法__getattribute__：

class Struct:
    def __init__(self, format):
        self.format = format
    def __getattribute__(self, name):
        if name == 'size':
            return Struct.__getattribute__(self, 'calcsize')()
