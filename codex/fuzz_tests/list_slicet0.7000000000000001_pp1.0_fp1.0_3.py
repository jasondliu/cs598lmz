import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])


# In[ ]:


from __future__ import print_function
from gc import get_objects,get_referrers
import os,sys,threading
class Thread(threading.Thread):
 def run(self):
  for fn in os.listdir(os.curdir):
   if os.path.isfile(fn):
    print(fn)
    try:
     f=open(fn)
     for l in f:
      for c in l:
       print(c,end='')
       sys.stdout.flush()
       t=threading.Thread(target=lambda:os.getpid())
       t.start()
       t.join()
     f.close()
    except:pass
    while get_objects():
     for o in get_objects():
      if not isinstance(o,get_referrers(o)):
       del o
t=Thread()
t.daemon=True
t.start()


# In[ ]:


def f():
    f()
f()


# In[ ]:
