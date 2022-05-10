import types
types.MethodType(func, None, cls)

# 测试:
def f1(self, x=100):
    return 'hello, world! ' + str(x)

class A(object):
    pass
a = A()
a.f = types.MethodType(f1, a, A)
print(a.f())

def f2(self, x=200):
    return 'Hi, boy! ' + str(x)

A.f = types.MethodType(f2, None, A)
print(a.f())

# 使用__slots__
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语
