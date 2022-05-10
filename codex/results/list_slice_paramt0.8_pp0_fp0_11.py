import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(lst))
keepali0e.append(weakref.ref(lst[0]))
d=weakref.ref(a,callback=callback)
keepali0e[0]=d


import gc
gc.collect()
for i,node in enumerate(gc.get_referrers(a)):
  print "%d: %s"%(i,type(node).__name__)
  if isinstance(node,dict):
    for k,v in node.iteritems():
      print k,v
raw_input()
