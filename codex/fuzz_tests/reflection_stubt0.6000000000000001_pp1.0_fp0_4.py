fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()"""

def test_code_attr_set_to_int():
    """>>> fn = lambda: None
    >>> fn.__code__ = 12
    Traceback (most recent call last):
        ...
    TypeError: readonly attribute"""

def test_code_attr_set_to_class():
    """>>> fn = lambda: None
    >>> fn.__code__ = type
    Traceback (most recent call last):
        ...
    TypeError: readonly attribute"""

def test_code_attr_set_to_code():
    """>>> fn = lambda: None
    >>> fn.__code__ = fn.__code__
    Traceback (most recent call last):
        ...
    TypeError: readonly attribute"""

def test_code_attr_set_to_func():
    """>>> fn = lambda: None
    >>> fn.__code__ = type
    Traceback (most recent call last):
        ...
    TypeError: readonly attribute"""

def test_code_attr_set_to_method():
    """>>> fn =
