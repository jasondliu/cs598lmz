import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
q=lst[0]
del q
#如果keepalive不是空的，那么对象就不会被销毁，因为对象中还有引用
print(keepali0e)
