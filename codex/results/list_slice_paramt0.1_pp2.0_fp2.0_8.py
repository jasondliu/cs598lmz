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
#['<weakref at 0x7f9f9c0a7c78; to 'A' at 0x7f9f9c0a7c50>']

#结论：
#1.当一个对象的引用计数为0时，它会被回收，但是它的弱引用不会被回收
#2.当一个对象的引用计数为0，并且它的弱引用也为0时，它会被回收
#3.当一个对象的引用计数为0，并且它的弱引用也为0时
