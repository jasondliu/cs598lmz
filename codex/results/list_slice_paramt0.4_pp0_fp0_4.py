import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]='a'
keepali0e.append(weakref.ref(a,callback))
lst[0]='b'
keepali0e.append(weakref.ref(a,callback))
lst[0]='c'
keepali0e.append(weakref.ref(a,callback))
lst[0]='d'
keepali0e.append(weakref.ref(a,callback))
lst[0]='e'
keepali0e.append(weakref.ref(a,callback))
lst[0]='f'
keepali0e.append(weakref.ref(a,callback))
lst[0]='g'
keepali0e.append(weakref.ref(a,callback))
lst[0]='h'
keepali0e.append(weakref.ref(a,callback))
lst[0]='i'
keepali0e.append(weakref.ref(a,callback))
lst[0]='j'
keepali0e.append(
