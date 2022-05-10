fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = ''

def f(*args):
    pass


class F():

    def fn(*args):
        pass
if not hasattr(sys, 'gettrace'):
    del F
    del f
    del fn
    del F.fn
    del f.func_code
    del fn.__code__
    del f.func_closure
    del f.__defaults__
    del fn.__defaults__
    del f.func_defaults
    del fn.__globals__
    del fn.__dict__
    del f.func_dict
    del f.func_name
    del fn.__name__
    del fn.__qualname__
    del f.func_doc
    del fn.__doc__
else:

    class C(object):

        def fn(*args):
            pass
    F.__module__ = 'name'
    C.fn.__module__ = 'name'
    F.fn.__module__ = 'name'
    F.fn.__qualname__
