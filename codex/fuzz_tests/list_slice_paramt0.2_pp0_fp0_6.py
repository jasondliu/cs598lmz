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

#结果：
#['<__main__.A object at 0x7f4b4c4a7a58>']

#结论：
#当一个对象的引用计数为0时，会调用它的__del__方法，但是如果在__del__方法中，对该对象的引用计数进行了操作，那么这个对象就会被垃圾回收器放弃回收，
#因为它的引用计数不为0，所以它的__del__方法也不会被
