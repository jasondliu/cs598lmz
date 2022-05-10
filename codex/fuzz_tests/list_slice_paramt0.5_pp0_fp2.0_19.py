import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
print(keepali0e)
print(len(lst))
print(len(keepali0e))
lst=[]
keepali0e=[]
for i in range(100):
    lst.append(A())
    keepali0e.append(weakref.ref(lst[-1],callback))
    del lst[-1]
print(len(lst))
print(len(keepali0e))
lst=[]
keepali0e=[]
for i in range(100):
    lst.append(A())
    keepali0e.append(weakref.ref(lst[-1],callback))
    del lst[-1]
print(len(lst))
print(len(keepali0e))
lst=[]
keepali0e=[]
for i in range(100):
    lst.append(A())
    keepali0e.append(weakref.ref(lst[-1],callback))
    del lst[-1]
