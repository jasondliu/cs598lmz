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
del keepali0e
print lst

#结果：['', '']
#解释：
#在第一次删除a的时候，a.c的引用计数减一，但是a.c的引用计数还是大于0，所以不会被回收，所以lst中的第一个元素不会被删除；
#在第二次删除a.c的时候，a.c的引用计数减一，但是a.c的引用计数还是大于0
