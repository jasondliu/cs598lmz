fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__doc__ = 'bar'
fn.__dict__ = {}
fn.__module__ = 'baz'
fn.__defaults__ = ()
fn.__closure__ = ()
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__globals__ = {}
fn.__get__ = lambda self, obj, type=None: None
fn.__set__ = lambda self, obj, value: None
fn.__delete__ = lambda self, obj: None
fn.__call__ = lambda self, *args, **kwargs: None
fn.__len__ = lambda self: 0
fn.__length_hint__ = lambda self: 0
fn.__getitem__ = lambda self, key: None
fn.__missing__ = lambda self, key: None
fn.__setitem__ = lambda self, key, value: None
fn.__delitem__ = lambda self, key: None
fn.__iter__ = lambda self: None
fn.__reversed__
