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

#['']

#结论：
#1.弱引用的回调函数只有在引用的对象被回收时才会被调用
#2.弱引用的回调函数只有在引用的对象被回收时才会被调用
#3.弱引用的回调函数只有在引用的对象被回收时才会被调用
#4.弱引用的回调函数只有在引用的对象被回收时才会
