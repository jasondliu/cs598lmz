fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: 0).__code__
fn.__name__ = gi.gi_name = '<lambda>'
fn.__qualname__ = gi.gi_qualname = '<lambda>'
fn.__annotations__ = gi.gi_annotations = {}
fn.__kwdefaults__ = gi.gi_kwdefaults = None
fn.__defaults__ = gi.gi_defaults = ()
fn.__closure__ = gi.gi_closure = None
fn.__globals__ = gi.gi_globals = {}
fn.__dict__ = gi.gi_dict = {}
fn.__module__ = gi.gi_module = '<lambda>'
fn.__text_signature__ = gi.gi_text_signature = '(...)'
fn.__get__ = gi.gi_get = lambda self, obj, type=None: self
fn.__self__ = gi.gi_self = None
fn.__weakref__ = gi.gi_weakrefl
