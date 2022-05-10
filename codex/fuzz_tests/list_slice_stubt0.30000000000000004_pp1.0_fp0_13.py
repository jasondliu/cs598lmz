import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print len(lst)

#结果为1
#因为在创建弱引用时，会检查对象是否有强引用，如果有，则不会被回收，所以不会触发回调函数

#示例2
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print len(lst)

#结果为1
#因为在创
