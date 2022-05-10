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

#['']

#按照上面的例子，可以看出，在删除对象a的时候，a的弱引用被触发，但是a.c的弱引用并没有被触发，这是因为a.c的弱引用指向的是a，而a并没有被删除，所以a.c的弱引用没有被触发。

#下面的例子演示了弱引用的一个特
