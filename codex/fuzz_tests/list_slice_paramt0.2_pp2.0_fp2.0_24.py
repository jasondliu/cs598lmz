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

#结果：['a']

#结论：当一个对象的引用计数为0时，会调用__del__方法，但是如果这个对象还存在弱引用，那么这个对象不会被销毁，
#直到所有的弱引用都被销毁，这个对象才会被销毁。

#弱引用的作用：
#1.当一个对象的引用计数为0时，会调用__
