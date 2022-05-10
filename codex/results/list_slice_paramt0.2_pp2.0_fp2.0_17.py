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
del a.c
print lst

#结果：['\x00']

#结论：
#1.弱引用的回调函数是在对象被回收时调用的，而不是在弱引用被回收时调用的。
#2.弱引用的回调函数是在对象被回收时调用的，而不是在弱引用被回收时调用的。
#3.弱引用的回调函数是在对象被回收时
