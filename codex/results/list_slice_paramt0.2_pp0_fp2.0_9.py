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
#['<weakref at 0x7f6d9c0e9d88; to 'A' at 0x7f6d9c0e9c50>']

#结论：
#1.当一个对象的引用数为0时，该对象会被回收
#2.当一个对象的引用数为0时，该对象的弱引用会被回收
#3.当一个对象的引用数为0时，该对象的弱引用会被回收，并且会调用回调函数
#4.当一个对
