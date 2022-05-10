import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：['abc']

#结论：
#1.当一个对象的引用计数为0时，会调用__del__方法，但是如果__del__方法中又引用了该对象，则该对象的引用计数不为0，不会被回收
#2.当一个对象的引用计数为0时，会调用__del__方法，但是如果__del__方法中又引用了该对象，则该对象的引用
