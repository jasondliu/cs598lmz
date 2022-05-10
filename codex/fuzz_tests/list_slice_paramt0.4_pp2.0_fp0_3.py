import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：['', '']
#分析：
#当del a时，a变成了垃圾，但是因为a.c=a，a被a.c引用，所以a不会被回收，
#而a.c也不会被回收，因为a.c被keepali0e引用，所以a.c不会被回收，
#当a.c被回收时，回调函数被调用，所以lst[0]被删除，
#当del lst[0]时，lst
