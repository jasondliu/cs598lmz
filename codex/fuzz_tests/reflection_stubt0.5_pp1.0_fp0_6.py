fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
 
#-----------------------------------------------------------------------------
# The doctests in this module
#-----------------------------------------------------------------------------

__test__ = {
    'getargspec' : '''

>>> from inspect import getargspec
>>> def f(a, b=2, c=3, *d): pass
>>> getargspec(f)
(['a', 'b', 'c'], 'd', None, (2, 3))

>>> def f(a, b=2, c=3, *d, **e): pass
>>> getargspec(f)
(['a', 'b', 'c'], 'd', 'e', (2, 3))

>>> def f(a, b, c=3, *d, **e): pass
>>> getargspec(f)
(['a', 'b', 'c'], 'd', 'e', (3,))

>>> def f(a, b, c=3, *, d, **e): pass
>>> getargspec(f)
(['a', 'b', 'c'], None, 'e', (3,), '
