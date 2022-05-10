import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepal1e.append(a)
lst.append(lst)
keepal1e.append(lst)
#print len(lst)
wref=weakref.ref(lst,callback)
#print repr(wref)
#print repr(wref())
del lst
#pri
