import types
types.MethodType(test, 'class')
test('instance')

# 测试绑定函数
def add(x, y):
    return x + y
print(add(1, 2))

add2 = types.MethodType(add, 2)
print(add2(3))
print(add2(4))

# 测试绑定类方法
class Foo(object):
    def __init__(self):
        self.name = 'foo'

    def hello(self):
        print('hello', self.name)

f = Foo()
f.hello()

hello = types.MethodType(Foo.hello, f)
hello()

# 测试绑定静态方法
class Bar(object):
    @staticmethod
    def hello():
        print('hello world')

bar = Bar()
bar.hello()

hello = types.MethodType(Bar.hello, bar)
hello()
