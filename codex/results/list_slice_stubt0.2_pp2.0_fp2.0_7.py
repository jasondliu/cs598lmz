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

#结果
#['']

#结论
#当一个对象的引用计数为0时，如果这个对象的__del__方法中有对其他对象的引用，则这个对象的引用计数不会为0，
# 即使这个对象的引用计数为0，也不会被回收，直到__del__方法执行完毕，这个对象的引用计数才为0，才
