import types
types.MethodType(func, None, cls)

# 要删除属性，用 delattr() 方法：
delattr(cls, 'name')

# 使用 dir() 方法，它返回一个包含字符串的 list，每个字符串为类对象的一个属性。
dir('ABC')

# 仅仅把属性和方法列出来是不够的，配合 getattr()、setattr() 以及 hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):

