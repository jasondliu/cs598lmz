import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print lst

#这个例子中，a对象引用了自身，导致在删除a之前，它不可能被回收，
#而lst本身引用了a，所以在删除lst前，a不可能被回收。
#只有当lst被回收时，它才会调用callback方法，
#因为callback方法会将lst中的元素删除，
#所以lst本身也会被回收，同时回收了a，所以对象a
