import types
types.MethodType(func, obj)
# 这里，我们创建了一个函数func，将其作为方法绑定到了obj上，并赋值给obj.f。现在，obj.f()调用将调用我们创建的func函数。

# 此外，通过types.MethodType()方法，我们还可以给一个类绑定方法，对于类的方法，第一个参数需要是一个实例对象。
def func(self,name='world'):
    print('hello, %s' % name)

Hello = type('Hello',(object,),dict(hello=
