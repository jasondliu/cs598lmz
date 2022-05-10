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

#结果：['\x00']

#结论：当a被删除时，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c引用的是a，a.c
