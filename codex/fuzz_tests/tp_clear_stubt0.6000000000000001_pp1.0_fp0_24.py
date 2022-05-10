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

func()
"""

def test_late_binding_bug():
    """
    >>> def f():
    ...     pass
    >>> f.__module__ = 3
    >>> import gc
    >>> gc.collect()

    """

import sys

def test_sys_exc_info_bug():
    """
    >>> '__module__' in sys.exc_info()[2].tb_frame.f_locals
    False
    >>> '__module__' in sys.exc_info()[2].tb_frame.f_locals
    False
    """

def test_builtin_exceptions_have_module():
    """
    >>> try:
    ...     raise KeyError
    ... except KeyError:
    ...     assert KeyError.__module__ == 'exceptions'
    """

def test_builtin_exceptions_have_module_2():
    """
    >>> try:
    ...     raise KeyError
    ... except KeyError:
    ...     assert KeyError.__module__ == '
