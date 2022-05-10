import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.a=a
keepalive.append(a)
a.b=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print len(lst)
lst.append(str())
del lst[1]
lst.append(str())
print len(lst)
lst.append(str())
lst[0]='x'*(sys.getrecursionlimit()+1)
print len(lst)
lst.append(str())
print len(lst)
lst[0]=lst
print len(lst)
lst.append(str())
print len(lst)
lst[0]=weakref.ref(lst,callback)
print len(lst)
lst.append(str())
print len(lst)
lst[0]=lst[0]
print len(lst)
lst.append(str())
print len(lst)
lst[0]=lst[0]
