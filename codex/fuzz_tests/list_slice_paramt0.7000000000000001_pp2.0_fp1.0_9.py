import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
gc.collect()
print lst

a=A()
a.c=a
lst.append(weakref.ref(a,callback))
gc.collect()
print lst
keepali0e=[]
gc.collect()
print lst

#测试函数引用自身
def f(n):
    if n==1:
        return n
    else:
        return n*f(n-1)
print f(5)

#测试引用自身的类
class F:
    def __init__(self,n):
        self.n=n
    def f(self):
        if self.n==1:
            return self.n
        else:
            return self.n*self.f()
f=F(5)
print f.f()

#测试引用自身的类属性
class F:
    def __init__(self
