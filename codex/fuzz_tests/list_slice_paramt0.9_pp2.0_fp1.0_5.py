import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)          #注册对象a引用
keepali0e.append(lst)

print(keepali0e[0](),keepali0e[1]())
print(keepali0e[1]())
del a
print(keepali0e[0](),keepali0e[1]())
print(keepali0e[1]())
del lst
print(keepali0e[1]())
