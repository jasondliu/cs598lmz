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
#['<__main__.A object at 0x7f9a9b7c6b50>']

#结论：
#1.当一个对象的引用计数为0时，它会被回收
#2.当一个对象的引用计数为0时，它的弱引用计数不为0时，它不会被回收
#3.当一个对象的引用计数为0时，它的弱引用计数为0时，它会被回收
#4.当一个对象的引用计
