import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.c=None
keepali0e.pop()
del a
lst_after=lst[:]
lst_after.append('end')
assert lst_after==['']
assert 'end'in lst_after
assert 'end'not in lst
assert 'end'in lst_after
assert 'foo'not in lst_after
assert 'foo'not in lst
