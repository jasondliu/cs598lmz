import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst))

print(len(lst))
del a
print(len(lst))


##4.4.2 弱引用计数

def weak_ref_check(obj):
    c=weakref.getweakrefcount(obj)
    m=getattr(obj,'__weakref__',None)
    return bool(c)&bool(m)
def weak_ref_check2(obj):
    c=weakref.getweakrefcount(obj)
    s=weakref.getweakrefs(obj)
    return bool(c)&bool(s)

##4.4.3 属性引用
import weakref
class A(object):
    def __init__(self,b):
        self.b=b
def callback(x):print x
a=A(42)
w=weakref.ref(a,callback)
print(w())
a.b=50
print(w())
a=
