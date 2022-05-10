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

#结果：['<__main__.A object at 0x7f5f5c0f5e10>']
#结论：循环引用的对象，不会被回收

#结论：循环引用的对象，不会被回收

#结论：循环引用的对象，不会被回收

#结论：循环引用的对象，不会被回收

#结论：循环引用的对象，不会被回收

#
