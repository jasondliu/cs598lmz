import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
a.d=b
b.d=b
a.a=keepali0e;a.b=lst;b.a=keepali0e;b.b=lst
keepali0e.append(weakref.ref(b,callback));del a,b
lst[0]='a'*10+'\x0b'*4+'a'*256+'\0'*128
a_weakref=weakref.ref(a,callback)del a,lst
a=a_weakref()
b=a.d
a.a=a
a.b=b
a.e=a
b.e=b
b.a=a
b.b=b
b.e=b
a.d=a
b.d=b
a.c=b
b.c=a
print a.e.e.a.b.e.e.a.a.a.a.b.d.e.f,b.e.e.a.b.e.e.
