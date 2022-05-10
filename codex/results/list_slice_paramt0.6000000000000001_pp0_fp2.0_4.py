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
print(len(lst))
del keepali0e
print(len(lst))

#这里通过循环引用模拟了一个内存泄露,在删除a时,因为a.c还指向a,所以a不能被回收,
#所以循环引用导致的内存泄露

#所以,可以通过弱引用来解决这个问题
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
