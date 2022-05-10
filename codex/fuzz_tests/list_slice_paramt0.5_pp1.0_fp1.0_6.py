import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del a.c
del keepali0e
print len(lst)

#3.3
def f(x,y):
    return x+y
def g(x,y):
    return x*y
def h(x,y):
    return x-y
def i(x,y):
    return x/y

def apply(func,x,y):
    return func(x,y)

print apply(f,2,3)
print apply(g,2,3)
print apply(h,2,3)
print apply(i,2,3)

#3.4
class A(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return A(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return A(self
