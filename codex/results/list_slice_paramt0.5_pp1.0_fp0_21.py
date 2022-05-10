import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
print(lst)
del a
print(lst)

lst=[]
def callback(x):del lst[0]
a=A()
a.c=a
lst.append(a)
print(lst)
del a
print(lst)

lst=[]
def callback(x):del lst[0]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

lst=[]
def callback(x):del lst[0]
a=A()
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

lst=[]
def callback(x):del lst[0]
a=A()
lst.append(weakref.ref(a,callback))
print(lst)
a.c=a
print(lst)
del a
print(lst
