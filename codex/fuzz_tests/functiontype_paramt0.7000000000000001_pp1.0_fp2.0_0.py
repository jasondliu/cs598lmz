from types import FunctionType
list(FunctionType(b,globals(),'b')())

# 创建一个类对象
def fn(self,name='world'):
    print('Hello, %s'%name)
Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
h.hello()
