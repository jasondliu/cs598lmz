import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
del keepali0e[2]
del keepali0e[1]
del keepali0e[0]
raise ValueError("gone through del without calling callback 0")
_pyw_reftime=0
