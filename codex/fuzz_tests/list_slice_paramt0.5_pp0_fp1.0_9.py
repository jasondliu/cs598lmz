import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(lst[0],callback))
del keepali0e
del a
del lst
print("end")

'''
class A(object):pass
def callback(x):print("callback")
a=A()
a.c=a
b=a
keepali0e=[weakref.ref(a,callback),weakref.ref(a.c,callback),weakref.ref(b,callback)]
del keepali0e
del a
del b
print("end")
'''
