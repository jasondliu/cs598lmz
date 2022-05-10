import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
del keepalive
lst[0]=callback
del lst
gc.collect()
"""

def test_weakref_callback_with_del():
    """
    >>> import gc
    >>> import weakref
    >>> class A(object):pass
    >>> def callback(x):del lst[0]
    >>> keepalive=[]
    >>> lst=[str()]
    >>> a=A()
    >>> a.c=a
    >>> keepalive.append(a)
    >>> del a
    >>> del keepalive
    >>> lst[0]=callback
    >>> del lst
    >>> gc.collect()
    """

def test_weakref_callback_with_del_2():
    """
    >>> import gc
    >>> import weakref
    >>> class A(object):pass
    >>> def callback(x):del lst[0]
    >>> keepalive=[]
    >>> lst=[str()]
    >>> a=A()
    >>> a.c=a

