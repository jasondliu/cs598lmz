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

#类的属性和实例属性
class A(object):
    x=1
    def __init__(self,y):
        self.y=y
a=A(2)
print(a.x,a.y)
a.x=11
print(a.x,A.x)
del a.x
print(a.x,A.x)
del A.x
print(a.x)

#类的属性和实例属性
class A(object):
    x=1
    def __init__(self,y):
        self.y=y
a=A(2)
print(a.x,a.y)
a.x=11
print(a.x,A.x)
del a.x
print(a.x,A.x)
del A.x
print(a.x)


