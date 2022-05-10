import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
del keepalive
print lst

#output:
#[str(), <weakref at 0x7f9a9f9c7e18; to 'A' at 0x7f9a9f9c7f28>]

#结论：
#1.weakref.ref()的第二个参数是回调函数，当弱引用对象被回收时，会调用这个回调函数，回调函数的参数是弱引用对象的引用
#2.弱引用对象的引用是弱引用对象本身，而不是弱
