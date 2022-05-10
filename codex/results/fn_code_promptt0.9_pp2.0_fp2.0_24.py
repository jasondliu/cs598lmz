fn = lambda: None
# Test fn.__code__
""">>> fn.__code__.co_varnames
('a', 'b', 'c')
>>> fn.__code__.co_argcount
3
>>> fn.__code__.co_filename
'<stdin>'

"""

# Test Test fns.__code__.co_firstlineno
def f():
    """
    test f.
    """,
    pass
"""
>>> print(f.__code__.co_firstlineno)
1
"""

def h(a, b = (), c = None):
    """
    test h.
    """
    pass

"""
>>> h.__code__.co_varnames
('a', 'b', 'c')
>>> h.__code__.co_argcount
3
"""

"""
## Test fn.__defaults__, fn.__closure__

>>> def outer(x):
...     y = 10
...     def inner():
...         print(x+y)
...     return inner
...
>>> outer(1)()
11
>>> outer(1
