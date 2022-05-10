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

#结果：
#['<__main__.A object at 0x7f8e7c0c1e10>']
#这个结果说明，当a被删除时，a.c引用的是a，所以a.c也被删除，所以a.c也被删除，所以a.c也被删除，所以a.c也被删除，所以a.c也被删除，所以a.c也被删除，所以a.c也被删除，所以a.c也被删除
