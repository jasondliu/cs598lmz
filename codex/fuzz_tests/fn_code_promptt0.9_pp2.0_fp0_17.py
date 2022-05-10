fn = lambda: None
# Test fn.__code__.co_firstlineno - it's too new for 2.4
try:
    fn.__code__.co_firstlineno
    at_lineno = ' at line %s'
except AttributeError:
    at_lineno = ''

def assert_raises(exc, fun, *args, **kwds):
    """Fail unless exception of class exc is thrown by fun(*args, **kwds).

    Return the exception that is raised.  Equivalent to
    assertRaises(exc, lambda: fun(*args, **kwds)).
    """
    try:
        fun(*args, **kwds)
    except exc as e:
        return e
    except BaseException as e:
        raise AssertionError("%r raised instead of %r" % (e, exc))
    else:
        if hasattr(fun, '__name__'):
            exc_name = fun.__name__
        else:
            exc_name = str(fun)
        raise AssertionError("%s not raised" % exc_name)

def skip(msg):

