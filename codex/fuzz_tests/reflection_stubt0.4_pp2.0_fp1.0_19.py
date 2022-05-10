fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__globals__ = globals()
fn.__name__ = 'fn'
fn.__doc__ = 'fn'
fn.__module__ = '__main__'
fn.__dict__ = {}

# 使用函数模拟类
class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('hello, my name is %s, I am %s years old' % (self.name, self.age))

# 函数模拟类
def A(name, age):
    def say_hello():
        print('hello, my name is %s, I am %s years old' % (name, age))
    return say_hello

# 使用函数模拟类
a = A('jack', 18)
a.say_hello()

# 使用
