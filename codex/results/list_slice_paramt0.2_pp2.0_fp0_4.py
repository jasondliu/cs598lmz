import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
gc.collect()
print lst

#这个例子中，a对象的弱引用被放在keepalive中，这样就不会被回收。
#因为a对象的弱引用被放在keepalive中，所以a对象的弱引用不会被回收，
#所以a对象不会被回收，所以a.c对象不会被回收，所以a.c.c对象不会被回收，
#所以a.c.c.c对象不会被
