import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
tracker=weakref.ref(a,callback)
print len(lst)
print keepali0e[0]() is a
del a
gc.collect()
print lst[0]
print keepali0e[0]()


#获取弱引用
print weakref.getweakrefcount(a)
print weakref.getweakrefs(a)
