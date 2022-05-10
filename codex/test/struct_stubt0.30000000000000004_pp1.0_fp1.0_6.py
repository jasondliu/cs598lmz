from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 创建一个空类
class MyEmptyClass:
    pass

# 创建一个空类
MyEmptyClass = type('MyEmptyClass', (), {})

# 创建一个类
class MyClass:
    # 创建一个类属性
    class_attr = 'class_attr'
    # 创建一个实例属性
    def __init__(self):
        self.instance_attr = 'instance_attr'

# 创建一个类
MyClass = type('MyClass', (), {'class_attr': 'class_attr', '__init__': lambda self: setattr(self, 'instance_attr', 'instance_attr')})

# 创建一个类
