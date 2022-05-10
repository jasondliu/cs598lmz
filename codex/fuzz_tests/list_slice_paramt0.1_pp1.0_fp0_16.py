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
#['<__main__.A object at 0x0000000003E9C908>']

#结论：
#当一个对象的引用计数为0时，会调用__del__方法，但是如果这个对象有循环引用，那么这个对象的引用计数不会为0，也就不会调用__del__方法，
#这个对象就会成为垃圾，但是不会被回收，这个对象会一直存在，
