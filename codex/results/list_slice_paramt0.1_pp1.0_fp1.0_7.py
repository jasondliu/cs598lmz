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
#['<__main__.A object at 0x7f8c9c0d5b90>']

#结论：
#当一个对象的引用计数为0时，会调用__del__方法，但是如果对象的引用计数不为0，即使对象的引用计数为0，也不会调用__del__方法。
#当一个对象的引用计数为0时，会调用__del__方法，但是如果对象的引用计数不为0，
