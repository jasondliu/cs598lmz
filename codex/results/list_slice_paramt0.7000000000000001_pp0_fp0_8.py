import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))

import os,sys,gc
os.environ['PYTHONINSPECT'] = '1'
os.environ['PYTHONSTARTUP'] = '1'
interact()
