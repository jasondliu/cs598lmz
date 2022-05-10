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
#['<__main__.A object at 0x0000000003D9B908>']

#结论：
#当一个对象的引用计数为0时，会调用__del__方法，但是如果对象的__del__方法中又引用了该对象，则该对象的引用计数不为0，不会调用__del__方法，
#这样就会导致内存泄漏。
#所以，在__del__方法中不要引用该对象。
