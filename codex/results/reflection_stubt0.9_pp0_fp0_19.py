fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
del i, gi, fn

def doctest_suite():
    import sys
    import doctest
    from . import _py_compat

    optionflags = (doctest.NORMALIZE_WHITESPACE |
                   doctest.ELLIPSIS)

    if sys.platform == 'darwin':
        # Don't check error messages on OS X.
        optionflags = optionflags | doctest.IGNORE_EXCEPTION_DETAIL

    return doctest.DocTestSuite(optionflags=optionflags)


# Nose is not supported on Python 3.
try:
    import nose
except ImportError:
    pass
else:
    def nose_suite():
        import os
        import pkg_resources

        import nose.loader as loader
        import nose.suite as suite
        import nose.config as config

        env = {}
        defaultTest = pkg_resources.resource_filename(
            'test.test_support', 'defa
