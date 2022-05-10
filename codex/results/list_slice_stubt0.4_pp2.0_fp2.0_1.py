import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a.c,callback))
keepali0e.append(a.c)
del a
del keepali0e
gc.collect()
print(len(lst))

#运行结果是1，说明a.c的弱引用被回调函数删除了
#回调函数的参数是弱引用对象，即弱引用对象对应的对象被回收时，回调函数被调用
#回调函数的参数是弱引用对象，回调函数被
