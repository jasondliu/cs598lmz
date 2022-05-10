import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.l=weakref.ref(lst,callback)
keepalive.append(a)
del a
import gc
gc.collect()

#python -c "import weakref; class A(object):pass; def callback(x):del lst[0]; keepalive=[]; lst=[str()]; a=A(); a.c=a; a.l=weakref.ref(lst,callback); keepalive.append(a); del a; import gc; gc.collect()"

#python -c "import weakref; class A(object):pass; def callback(x):del lst[0]; keepalive=[]; lst=[str()]; a=A(); a.c=a; a.l=weakref.ref(lst,callback); keepalive.append(a); del a; import gc; gc.collect()"
#python -c "import weakref; class A(object):pass; def callback(x):del lst[0]; keepalive=[]; lst=[str()]; a=A(); a.c=a;
