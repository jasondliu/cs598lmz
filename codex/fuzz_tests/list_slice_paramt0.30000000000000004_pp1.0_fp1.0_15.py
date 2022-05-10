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

#练习
#编写一个回调函数，以检查某个对象是否仍然存在，如果不存在，则将其从一个列表中删除
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
del a
print lst

#练习
#编写一个回调函数，以检查某个对象是否仍然存在，如果不存在，则将
