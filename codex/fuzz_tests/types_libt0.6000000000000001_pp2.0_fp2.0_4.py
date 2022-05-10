import types
types.SimpleNamespace(a=1)

#  类的实例化

# 实例化类的时候，会自动调用类的构造函数 __init__(self, ...)
class Foo:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print('Hello, ' + self.name)

# 实例化类的时候，会自动调用类的构造函数 __new__(cls, *args, **kwargs)
# 如果类中定义了 __new__ 方法， __new__ 方法会被调用，
# 然后 __init__ 方法会被
