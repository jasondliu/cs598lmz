import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
#结果：['a']
#结果：[]

#回调函数的参数是被弱引用的对象
import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
#结果：['a']
#结果：<__main__.A object at 0x00000000026D5B00>
#结果：[]

#回调函数的参数是被弱引用的对象
import weakref
class A(object):pass
