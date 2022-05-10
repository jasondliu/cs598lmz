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
"
TESTS="
>>> a=A()
>>> lst=['a']
>>> lst[:]=lst
>>> len(lst)
2
>>> a=A()
>>> lst=['a']
>>> lst[:]=[a,a]
>>> len(lst)
1
>>> lst[0] is a
True
>>> lst[:]=[a,a]
>>> len(lst)
1
>>> lst[0] is a
True
>>> lst[:]=[]
>>> lst
[]

>>> lst=[2,3,4]
>>> a=[1]
>>> a.extend(lst)
>>> a
[1, 2, 3, 4]
>>>
"""
