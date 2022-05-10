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

#结果为：['',<weakref at 0x7f7a8b3a2f88; dead>]
#结论：当引用计数为0时，调用回调函数，并将引用从列表中删除

#示例2
import weakref
class A(object):pass
def callback(x):print 'callback'
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
del keepalive
print lst

#结果为：['',<weakref at 0x7f7a
