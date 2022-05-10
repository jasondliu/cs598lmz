import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=weakref.ref(a,callback)
del a
print(str(weakref.getweakrefcount(lst[0])))
def test():a=lst[0]
for i in range(1000):test()
