import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
lst.append(a)
keepalive.append(lst)
lst.append(weakref.ref(a,callback))
del a
print len(lst)
print lst
print keepalive

#结果：
#1
#['']
#[['', <weakref at 0x7f8c0c0e6e30; to 'A' at 0x7f8c0c0e6d50>]]

#结论：
#1.weakref.ref的回调函数被调用的时机是在被引用的对象被回收的时候
#2.在回调函数中，被引用的对象已经被回收，所以不能
