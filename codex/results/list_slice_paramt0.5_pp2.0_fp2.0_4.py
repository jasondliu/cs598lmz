import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

#print(lst)
#print(keepali0e)
#print(keepali0e[0]())
#print(keepali0e[0]().c)

#print(weakref.getweakrefcount(keepali0e[0]))
#print(weakref.getweakrefcount(keepali0e[0]()))
#print(weakref.getweakrefcount(keepali0e[0]().c))

#print(weakref.getweakrefs(keepali0e[0]))
#print(weakref.getweakrefs(keepali0e[0]()))
#print(weakref.getweakrefs(keepali0e[0]().c))

class A(object):
    def __del__(self):
        print("A.__del__")

class B(A):
    def __del__(self):
        print("B.__del__")

def callback(x):
    print("callback")

a=A()
keepali0e=
