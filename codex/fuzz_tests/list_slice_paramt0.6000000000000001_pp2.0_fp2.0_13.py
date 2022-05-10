import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)

#程序员在编写程序时，需要注意，如果在一个类中定义了一个__del__方法，并且实例化时做了一个循环引用，那么垃圾回收器就不会再回收这个实例了，程序员需要自己手动的去处理这个循环引用。
