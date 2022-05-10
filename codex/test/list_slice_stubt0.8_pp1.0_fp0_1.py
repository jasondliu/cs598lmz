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
