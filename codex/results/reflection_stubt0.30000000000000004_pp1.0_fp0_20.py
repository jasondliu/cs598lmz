fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__dict__ = {}
fn.__doc__ = None
fn.__globals__ = {}
fn.__closure__ = None
fn.__module__ = '__main__'
fn.__defaults__ = None
fn.__kwdefaults__ = None
fn.__annotations__ = {}
fn.__dict__ = {}
fn.__weakref__ = None
fn.__class__ = &lt;class 'function'&gt;
</code>

