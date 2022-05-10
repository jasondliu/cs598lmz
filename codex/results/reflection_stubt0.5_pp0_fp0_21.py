fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__globals__ = fn.__closure__ = ()
fn.__name__ = fn.__qualname__ = '<lambda>'
fn.__module__ = '__main__'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__kwdefaults__ = None
fn.__annotations__ = {}
fn.__get__ = lambda: None
fn.__self__ = None
fn.__func__ = None
fn.__closure__ = ()
fn.__doc__ = None
fn.__text_signature__ = None
fn.__module__ = '__main__'
fn.__qualname__ = '<lambda>'
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__name__ = '<lambda>'
fn.__code__ = gi.gi_code
fn.__defaults__ = ()
fn.__globals__ = fn.__closure__ = ()
fn.__dict__ = {}
fn.__self__ = None
fn.
