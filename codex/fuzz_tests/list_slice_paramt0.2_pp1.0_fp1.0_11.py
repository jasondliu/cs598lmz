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
#['<weakref at 0x7f8b8c0b4d88; to 'A' at 0x7f8b8c0b4c10>']

#结论：
#1.当一个对象的引用计数为0时，会调用__del__方法
#2.当一个对象的引用计数为0时，会调用弱引用的回调函数
#3.当一个对象的引用计数为0时，会调用__del__方法，但是如果在__del__方法中引用了该对象，则该
