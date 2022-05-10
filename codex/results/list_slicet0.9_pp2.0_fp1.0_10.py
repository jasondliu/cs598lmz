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
print('lst',lst)
print(lst[:])
print('lst',lst)
print([x if isinstance(x,str) else x() for x in keepali0e])
print(type(x) for x in keepali0e)
"""
lst ['']
[]
lst []
['', None]
<generator object <genexpr> at 0x7fe6e4e6b3b8>
"""
