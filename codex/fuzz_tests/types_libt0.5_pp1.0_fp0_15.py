import types
types.MethodType(f, None, class1)

# 我们试试把上面的函数变成一个实例方法：
class1.f = types.MethodType(f, None, class1)
class1.f()

# 给一个实例绑定的方法，对另一个实例是不起作用的：
class1.f()
class2 = class1()
class2.f()

# 为了给所有实例都绑定方法，可以给class绑定方法：
def f(self):
    print('hello, world!')

class2.f = types.MethodType(f, None, class1)
class2.f()

# 通常情况下，上
