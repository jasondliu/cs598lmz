import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果为：['\x00']
#因为a.c=a，所以a的弱引用被a.c强引用，所以a不会被回收，所以lst中的元素不会被删除

#第二个例子
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果为：[]
#因为a.c=a，所以a的弱引用被a.c强引用
