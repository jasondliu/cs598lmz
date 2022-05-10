import ctypes

class S(ctypes.Structure):
    x = 1

class C(object):
    def __init__(self):
        self.x = 1

def test_ctypes_struct():
    """
    >>> def test():
    ...     s = S()
    ...     s.x = 2
    ...     return s
    >>> test()
    <__main__.S object at 0x...>
    >>> test()
    <__main__.S object at 0x...>
    """

def test_class():
    """
    >>> def test():
    ...     c = C()
    ...     c.x = 2
    ...     return c
    >>> test()
    <__main__.C object at 0x...>
    >>> test()
    <__main__.C object at 0x...>
    """

def test_class_with_struct():
    """
    >>> def test():
    ...     c = C()
    ...     c.x = 2
    ...     return c.x
    >>> test()
    2
    >>> test()
    2
    """

def test
