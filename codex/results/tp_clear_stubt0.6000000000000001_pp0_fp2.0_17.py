import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()
latefin.__module__
"""

def test_gc_r_dict():
    """
    >>> d = {}
    >>> d['key'] = d
    >>> import gc
    >>> gc.collect()
    >>> res = []
    >>> def func(d):
    ...     res.append(d)
    >>> gc.add_referrers(d, [func])
    >>> gc.collect()
    >>> res
    [{...}]
    """

def test_gc_r_dict_2():
    """
    >>> import gc
    >>> def func(d):
    ...     res.append(d)
    >>> res = []
    >>> d = {}
    >>> d['key'] = d
    >>> gc.add_referrers(d, [func])
    >>> gc.collect()
    >>> res
    [{...}]
    """

def test_gc_r_dict_3():
    """
    >>> import gc
    >>> def func(d):
    ...    
