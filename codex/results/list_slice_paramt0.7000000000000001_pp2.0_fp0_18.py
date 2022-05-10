import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a,callback))
a=None
import gc
gc.collect()

import weakref
d={}
def callback(x):del d["abc"]
d["abc"]=str()
keepali0e=weakref.ref(d["abc"],callback)
d=None
import gc
gc.collect()

import weakref
d={}
def callback(x):del d["abc"]
d["abc"]=str()
keepali0e=weakref.ref(d["abc"],callback)
del d["abc"]
import gc
gc.collect()

import weakref
d={}
def callback(x):del d["abc"]
d["abc"]=str()
keepali0e=weakref.ref(d["abc"],callback)
d["abc"]="xyz"
import gc
gc.collect()

import weakref
d={}
def callback(x):del d["abc"]
d["abc"]=str()
keepali0e=weakref.ref(d["abc
