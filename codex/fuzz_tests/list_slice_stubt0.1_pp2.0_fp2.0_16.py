import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
del keepalive
gc.collect()
print(lst)

#结果：
#['']

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它有一个循环引用，它就不会被回收，因为它的引用计数不为0，
#所以，当一个对象的引用计数为0时，它会被回收，但是如果它有一个循环引用
