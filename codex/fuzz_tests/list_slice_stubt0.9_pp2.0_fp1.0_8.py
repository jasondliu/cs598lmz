import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.tup=tuple([a])
a.lst=list([a])
a.dict={a:a}
a.comp=complex(a)
a.set=set([a])
a.frozenset=frozenset([a])
keepali1e.append(a.frozenset)
lst.append(WR(a,callback))
