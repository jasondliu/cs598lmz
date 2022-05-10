import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=weakref.WeakKeyDictionary()
a.d[a]=a
keepali0e.append(a)
a.e=weakref.WeakValueDictionary()
a.e[a]=a
keepali0e.append(a)
a.f=weakref.WeakSet()
a.f.add(a)
keepali0e.append(a)
wr=weakref.ref(a,callback)
del a
keepali0e[0]=lst
keepali0e[1]=wr
keepali0e[2]=callback
keepali0e[3]=weakref
keepali0e[4]=weakref.ReferenceType
keepali0e[5]=weakref.WeakValueDictionary
keepali0e[6]=weakref.WeakSet
keepali0e[7]=weakref.WeakKeyDictionary
keepali0e[8]=dict
keepali0e[9]=object
keepali0e[10]=type
keepali0e[11]=str
keepali0e[12]=A
keepali0e[13]=l
