import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
for i in range(1000):
    keepali0e.append(weakref.ref(a,callback))
    lst.append(str())
    a=lst[-1]
while lst:
    lst.append(str())
    a=lst[-1]
"""

def test_weakref_callback_with_del_local():
    """
    >>> import gc; gc.collect()
    >>> import weakref
    >>> lst = []
    >>> def callback(x):
    ...     lst.append(1)
    >>> a = [1, 2, 3]
    >>> b = [a, a]
    >>> keepalive = [a, b, b[0]]
    >>> keepalive.append(weakref.ref(a, callback))
    >>> del a
    >>> gc.collect()
    >>> len(lst)
    1
    """

def test_weakref_callback_with_dict_key():
