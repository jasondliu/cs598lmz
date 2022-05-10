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
#['<weakref at 0x00000000029F0E88; to 'A' at 0x00000000029F0E48>']

#结论：
#1.当引用计数为0时，对象会被回收
#2.当对象的引用计数为0时，对象会被回收，但是如果对象有循环引用，则不会被回收
#3.当对象的引用计数为0时，对象会被回收，但是如果对象有循环引
