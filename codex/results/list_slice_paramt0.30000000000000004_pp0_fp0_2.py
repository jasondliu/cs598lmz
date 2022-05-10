import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print(lst)

#结果：['', '']
#因为a.c是a的弱引用，所以a.c也会被回调函数删除

#第二个例子
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(a.c)
del a
print(lst)

#结果：['', '']
#因为a.c是a的弱引用，所以a.c也会被回调函
