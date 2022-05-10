import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
w=weakref.ref(a,callback)
del a
print(lst)

#结论：删除对象后，对象的弱引用会马上被回收，弱引用不会影响对象的回收
