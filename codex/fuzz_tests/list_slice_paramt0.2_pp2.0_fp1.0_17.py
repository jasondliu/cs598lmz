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

#结果：['\x00']

#结论：
#当对象a被删除时，a.c的弱引用被删除，但是a的弱引用没有被删除，所以lst中的元素没有被删除

#第二种情况：
#当对象a被删除时，a.c的弱引用被删除，但是a的弱引用没有被删除，所以lst中的
