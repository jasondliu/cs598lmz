import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst.append(str())
del lst


#gc.set_debug(gc.DEBUG_LEAK)

class A(object):
    pass

lst=[str()]

a=A()
a.c=a
lst.append(weakref.ref(a,lambda x: del lst[0]))

del a
lst.append(str())
#del lst


# 测试回调里嵌套调用引用
import weakref
class A(object):pass
def callback(x):callback.called=True
callback.called=False
a=A()
a.c=a
lst=[weakref.ref(a,callback)]
del a
del lst
print callback.called
