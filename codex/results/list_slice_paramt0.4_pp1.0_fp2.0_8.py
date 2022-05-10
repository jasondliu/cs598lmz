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
gc.collect()
print(lst)

# 可以看到，当有循环引用的时候，gc不会回收，所以callback不会被调用

# 改进，使用weakref.finalize

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.finalize(a,callback))
keepali0e.append(weakref.finalize(a.c,callback))
del a
gc.collect()
print(lst)

# 可以看到，当使用weakref.finalize的时候，finalize
