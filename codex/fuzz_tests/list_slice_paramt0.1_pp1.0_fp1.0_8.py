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
#['<__main__.A object at 0x7f8f8c0b7b90>']

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它有一个弱引用，那么它就不会被回收，直到弱引用被回收，这样就会导致内存泄露。
#所以，弱引用只能用于对象的引用计数为0时，还需要对它
