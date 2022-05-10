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

#结果：['\x00']

#结论：
#1.循环引用的对象，不会被回收
#2.循环引用的对象，弱引用的回调函数不会被调用
#3.循环引用的对象，弱引用的回调函数不会被调用，但是弱引用的对象会被回收

#结论1：循环引用的对象，不会被回收
#结论2：循
