import types
types.MethodType(f,None,Spam)

#给实例绑定方法
s = Spam()
s.bar = f
s.bar()

#给类绑定方法
Spam.bar = f
s.bar()

#给类绑定方法，需要使用MethodType
import types
def f(self,name='world'):
    print('Hello,%s.' % name)

Hello = type('Hello',(object,),dict(hello=f))
h = Hello()
h.hello()
