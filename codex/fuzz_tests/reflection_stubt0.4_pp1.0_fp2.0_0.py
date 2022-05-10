fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_frame)()
fn.__globals__ = {}
fn.__closure__ = (None,)
fn.__name__ = fn.__qualname__ = '<lambda>'
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = ()
fn.__dict__ = {}
fn.__module__ = '__main__'
fn.__text_signature__ = '()'
fn.__self__ = None
fn.__get__ = lambda s, o, t: s
fn.__call__ = lambda s, *a, **kw: s()
fn.__doc__ = None
fn.__set_name__ = lambda s, o, n: None
fn.__code__.co_code = b'\x00\x00S'
fn.__code__.co_consts = ()
fn.__code__.co_names = ()
fn.__code__.co_varnames = ()
fn.__code__.co_filename = '<
