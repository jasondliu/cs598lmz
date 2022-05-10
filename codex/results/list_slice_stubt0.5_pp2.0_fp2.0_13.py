import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
del a
del keepali0e
gc.collect()
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*10
lst[0]='a'*
