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
#['0']

#第二种情况：
#当引用计数为0，但是弱引用还存在的时候，这个对象就会被回收，并且调用回调函数
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#output:
#[]

#第三种情况：
#当引用计数为0，但是弱引用还存在的时候
