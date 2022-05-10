import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
import gc
gc.collect()
print lst

#['']

#这里的结果是，a.c指向a，a指向a.c，形成了循环引用，因此a和a.c都不会被回收，因此lst中的元素不会被删除。

#这里的结果是，a.c指向a，a指向a.c，形成了循环引用，因此a和a.c都不会被回收，因此lst中的元
