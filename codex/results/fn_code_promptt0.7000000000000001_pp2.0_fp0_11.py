fn = lambda: None
# Test fn.__code__ for Python < 2.6
test_fn.__code__ = None

# Python 2.6+
try:
    from functools import partial
except ImportError:
    # Python 2.4 or 2.5
    def partial(func, *args, **keywords):
        def newfunc(*fargs, **fkeywords):
            newkeywords = keywords.copy()
            newkeywords.update(fkeywords)
            return func(*(args + fargs), **newkeywords)
        newfunc.func = func
        newfunc.args = args
        newfunc.keywords = keywords
        return newfunc

# Python 2.6+
try:
    import unittest2 as unittest
except ImportError:
    # Python 2.4
    import unittest

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        json = None

# Python 2.5+
try:
    from hashlib import md5
except ImportError:
    from md5 import new as md
