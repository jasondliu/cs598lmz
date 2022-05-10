fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.func_code = gi.gi_code = type(lambda: 0)()
fn.__closure__ = gi.gi_frame.f_locals['__closure__'] = ()
fn.__defaults__ = gi.gi_frame.f_locals['__defaults__'] = ()
fn.__globals__ = gi.gi_frame.f_globals
fn.__name__ = fn.func_name = gi.gi_code.co_name = '_'
fn.__dict__ = gi.gi_frame.f_locals
fn.__doc__ = gi.gi_code.co_consts[0] if gi.gi_code.co_consts else ''
fn.func_closure = property(lambda self: self.__closure__)()
fn.func_code = property(lambda self: self.__code__)()
fn.func_defaults = property(lambda self: self.__defaults__)()
fn.func_globals = property(lambda self: self.__globals__)()
