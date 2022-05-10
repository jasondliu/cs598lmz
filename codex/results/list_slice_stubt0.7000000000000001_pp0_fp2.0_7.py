import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst.append(a)
assert lst[1] is a
lst.append(a.c)
assert lst[2] is a.c
keepali1e.append(lst[0])
keepali1e.append(lst[1])
del lst[2]
assert lst[1] is a.c
assert lst[0] is a
keepali2e.append(lst[0])
keepali2e.append(lst[1])
wref=weakref.ref(a,callback)
keepali3e.append(lst[0])
keepali3e.append(lst[1])
del a
if '__pypy__' in sys.builtin_module_names:
    gc.collect()
assert lst[1] is a.c
assert len(lst)==2
del a.c
gc.collect()
assert len(lst)==1
print 'passed'
