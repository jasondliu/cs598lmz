import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print lst

#output:
#['<weakref at 0x0000000003A7F7C8; to 'A' at 0x0000000003A7F5C8>']

#结论：
#1.python的weakref模块中的weakref.ref()方法的第二个参数是一个回调函数，当弱引用的对象被回收时，会调用这个回调函数
#2.这个回调函数的参数是一个弱引用对象，这个弱引用对象可以通过它的weakref.ref()方法获取到被
