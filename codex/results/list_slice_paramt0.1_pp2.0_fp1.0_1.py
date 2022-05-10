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
#['<weakref at 0x7f7f8c0b3e88; to 'A' at 0x7f7f8c0b3d68>']

#结论：
#1.弱引用的回调函数是在弱引用被回收时调用的，而不是引用的对象被回收时调用的
#2.弱引用的回调函数是在弱引用被回收时调用的，而不是引用的对象被回收时调用的
#3.弱引用的回调函数是在弱引用
