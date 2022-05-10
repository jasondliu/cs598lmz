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

#output:
#['<__main__.A object at 0x7f8d0c0d8c50>']

#结论：
#1.对于循环引用的对象，只有当其中一个对象被回收时，才会触发回调函数，而且回调函数中的参数是被回收的对象
#2.回调函数中的参数是被回收的对象，而不是弱引用对象
#3.回调函数中的参数是被回收的对象，
