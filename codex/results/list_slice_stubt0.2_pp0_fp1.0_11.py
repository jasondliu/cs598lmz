import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)
print(keepalive)

# 弱引用的目的是：在一个对象不再被引用的时候，自动将其回收。
# 弱引用的特点是：当一个对象的强引用被删除后，该对象的弱引用不会被删除，
# 只有当该对象的弱引用被删除后，该对象才会被回收。
# 弱引用的使用场景：
