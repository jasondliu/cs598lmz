import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.ref(a,callback)
del a
del keepalive

#栈上分配
lst=[]
for x in range(100000):lst.append([1,2,3,4,5,6,7,8,9,0])

#缓存
import weakref
class A(object):
    __slots__=('name','age','id')
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
class B(object):
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def __getstate__(self):
        return self.name,self.age,self.id
    def __setstate__(self,state):
        self.name,self.age,self.id=state
a=A('a',1,1)
b=B('a
