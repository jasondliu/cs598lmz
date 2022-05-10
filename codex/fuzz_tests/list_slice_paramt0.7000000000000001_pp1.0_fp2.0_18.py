import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]=a
del a
print len(lst)
print len(keepali0e)
lst[0].c=lst[0]

#3.1
import weakref
class A(object):pass
a=A()
s=weakref.WeakKeyDictionary()
s[a]=1
del a
print s

#3.2
import weakref
class A(object):pass
a=A()
s=weakref.WeakValueDictionary()
s['a']=a
del a
print s
