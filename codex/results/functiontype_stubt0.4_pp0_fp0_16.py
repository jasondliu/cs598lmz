from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(id(a))
print(id(b))

def foo():
    pass
print(type(foo))
print(type(foo) == FunctionType)
print(type(foo) == type(print))

from types import MethodType
def bar(self):
    pass

class Foo:
    pass

f = Foo()
f.func = MethodType(bar, f)
f.func()

# 给一个实例绑定的方法，对另一个实例是不起作用的
f1 = Foo()
f1.func()

# 为了给所有实例都绑定方法，可以给class绑定方法
def bar(self):
    print('bar')
Foo.func = bar
f = Foo()
f.func()

