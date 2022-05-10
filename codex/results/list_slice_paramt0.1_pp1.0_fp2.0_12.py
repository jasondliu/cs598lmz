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

#['']

#结论：
#1.当一个对象的引用计数为0时，它会被垃圾回收，但是它的__del__方法不会被调用
#2.当一个对象的引用计数为0时，它会被垃圾回收，但是它的__del__方法不会被调用
#3.当一个对象的引用计数为0时，它会被垃圾回收，但是它的__del__方法不会被调用

