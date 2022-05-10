import gc, weakref, inspect
    >>> class C(object): pass
    >>> class D(C): pass
    >>> c = C()
    >>> d = D()
    >>> d.c = c
    >>> d.cref = weakref.ref(c)
    >>> c.dref = weakref.ref(d)
    
    We can find out what, if anything, is referring to c:
    
    >>> x = gc.get_referrers(c)
    >>> x
    [{'c': <__main__.C object at 0x...>, 'cref': <weakref at 0x...; to 'C' at 0x...>},
    {'_C__cref': <weakref at 0x...; to 'C' at 0x...>},
    {'_D__c': <__main__.C object at 0x...>, '_D__cref': <weakref at 0x...; to 'C' at 0x...>},
    {'__repr__': <bound method D.__repr__ of <__main__.D object at 0
