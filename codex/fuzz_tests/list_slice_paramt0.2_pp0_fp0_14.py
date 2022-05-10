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
#['<__main__.A object at 0x7f5a7c0b5f90>']

#结论：
#1.如果一个对象的引用计数为0，但是它的__del__方法中又引用了其他对象，那么这个对象的引用计数就不会为0，
#这样就不会被回收，这样就会导致内存泄漏。
#2.如果一个对象的引用计数为0，但是它的__del__方法中又引用了
