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
gc.collect()
print(lst)

#结果：
#['']

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它的引用计数为0，但是它的__del__方法中又引用了其他对象，那么这个对象的引用计数就不为0，所以不会被回收。
#当一个对象的引用计数为0时，它会被回收
