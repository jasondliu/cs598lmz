import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
print 'refcount:',sys.getrefcount(lst[0])
del a.c
print lst
#运行结果：
#refcount: 5
#['
