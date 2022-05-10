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
#['<weakref at 0x7f8a9c0e9d88; to 'A' at 0x7f8a9c0e9c50>']

#结论：
#1.弱引用的回调函数会在对象被回收时被调用
#2.弱引用的回调函数会在对象被回收时被调用，而不是在弱引用被回收时被调用
#3.弱引用的回调函数会在对象被回收时被调用，而不是在弱
