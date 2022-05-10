import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]=a
a.c=None
keepali0e.append(weakref.ref(a,callback))
del a,lst
try:pass
except BaseException,msg:
 if isinstance(msg,TypeError):
  pass
 else:
  raise
"""

runtests(rscr, ascr, rdscr, 1, 2, 4)

rscr = """
l=[]
l.append(set())
l[0].add(l)
l[0].add(l[0])
"""

ascr = """
l=[]
l.append(set())
l[0].add(l)
l[0].add(l[0])
l[0].add(l[0])
del l
"""

rdscr = """
def callback(x):del l[0]
l=list()
l.append(set())
l[0].add(l)
l[0].add(l[0])
l[0].add(l[0])
s=weakref
