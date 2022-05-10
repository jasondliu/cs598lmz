import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]="abc"
del a
del keepali0e
print lst

#结果：
#['abc']
#这个结果的意思是，在python中，对象的引用计数器不会因为循环引用而增加，因此，当a对象被删除后，a.c对象也会被删除，因此，lst[0]中的字符串对象没有被删除。

#下面是一个循环引用的例子：
import weakref
class A(object):pass
def callback(x):del lst
