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
print(keepali0e)

#这个例子中，a.c=a，a引用自身，导致a不会被回收，lst中的str对象也不会被回收，因为lst中的str对象被a引用。
#当a被回收时，回调函数callback被调用，lst中的str对象被删除，这时lst中的str对象被回收。
#回调函数callback被调用时，lst中的str对象已经被回收，所以lst中
