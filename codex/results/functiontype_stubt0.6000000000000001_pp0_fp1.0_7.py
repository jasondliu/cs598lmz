from types import FunctionType
a = (x for x in [1])
b = FunctionType(a.gi_frame.f_code,a.gi_frame.f_globals)
print(b(1))
#1
'''

'''
#构造函数
def foo(a,b):
    print(a+b)
def foo2(a,b,c):
    print(a+b+c)
def __call__(self,*args,**kwargs):
    #print(self.func(*args,**kwargs))
    return self.func(*args,**kwargs)
    
class MyCall(object):
    def __init__(self,func):
        self.func = func
        
    def __call__(self,*args,**kwargs):
        return self.func(*args,**kwargs)
        
mycall = MyCall(foo)
mycall2 = MyCall(foo2)

print(mycall(1,2))
#3
print(mycall2(1,2,3))
#6
'''

'''
#
