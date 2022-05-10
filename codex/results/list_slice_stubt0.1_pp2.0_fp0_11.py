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
#当一个对象的引用计数为0时，它的__del__方法会被调用，但是如果它的__del__方法中又引用了它自己，那么它的引用计数就不会为0，所以它的__del__方法就不会被调用。
#所以，当一个对象的__del__方法中引用了它自己时，它的__del__方
