import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))#构建一个weakref对象,并放在一个列表中
lst

'''
'''
import weakref
keepali0e=[]
d={}
k=d.keys()
keepali0e.append(weakref.ref(k,lambda x:print("i am dead")))
del d
print("i am alive?")


#实现一个可调用的类
class IAmCallable(object):
    def __init__(self,a,b):
        self._a=a
        self._b=b
    def __call__(self):
        print("i am callable,a=%s,b=%s"%(self._a,self._b))

t=IAmCallable("tom","jerry")
t()
'''
'''
#实现任意进制转换
def fn(x,y):
    print
