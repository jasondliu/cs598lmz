import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
d=weakref.WeakKeyDictionary(a)
d[a]=1
d[str()]=1
d[1]=1
keepalive=[d,str(),int()]
lst[0]=str()
weakref.ref(lst[0],callback)
import gc,bugzz
gc.collect()
gc.collect()
gc.collect() 
del keepali0e,a,keepalive
del lst,callback
gc.collect()
</code>

