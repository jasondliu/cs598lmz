fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.func_code = gi.gi_code
fn.func_name = "<lambda>"
fn.func_defaults = []
fn.func_closure = gi.gi_frame.f_locals.values()
fn.__dict__ = {}
fn.func_dict = {}
</code>

