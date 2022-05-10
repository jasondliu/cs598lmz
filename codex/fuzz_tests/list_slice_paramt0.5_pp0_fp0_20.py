import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
#print(lst)
#print(keepali0e)
class A(object):
    def __init__(self,value,name):
        self.value=value
        self.name=name
        self.b=None
    def __repr__(self):
        return 'A(%r,%r,%r)'%(self.value,self.name,self.b)
    def __del__(self):
        print('A.__del__')
class B(object):
    def __init__(self,value,name):
        self.value=value
        self.name=name
        self.a=None
    def __repr__(self):
        return 'B(%r,%r,%r)'%(self.value,self.name,self.a)
    def __del__(self):
        print('B.__del__')
a=A(1,'a')
b=B(2,'b')
a.b=b
b.a=a
del a
del b
