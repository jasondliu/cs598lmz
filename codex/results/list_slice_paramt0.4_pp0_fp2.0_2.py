import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#类的定义
class A(object):
    def __init__(self,a):
        self.a=a
    def f(self):
        print(self.a)
a=A(100)
a.f()
print(a.a)

#类的继承
class A(object):
    def __init__(self,a):
        self.a=a
    def f(self):
        print(self.a)
class B(A):
    def __init__(self,a,b):
        super(B,self).__init__(a)
        self.b=b
    def f(self):
        super(B,self).f()
        print(self.b)
b=B(100,200)
b.f()
print(b.a,b.b)

#类的多态
class A(object):
    def f(self):
       
