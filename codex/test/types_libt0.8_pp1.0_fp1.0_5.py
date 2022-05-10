import types
types.ClassType

class MyClass:
    def x(self):
        pass

mc = MyClass()
mc.x()

import inspect
inspect.isclass(mc)
inspect.isclass(MyClass)
inspect.getclasstree([MyClass])

class MyClass:
    def __init__(self, x = 1, y = 2):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'MC(x=%s, y=%s)' % (self.x, self.y)

    def __str__(self):
        return 'x = %s, y = %s' % (self.x, self.y)

mc = MyClass(10)
