fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = gi.gi_frame.f_code = gi.gi_frame.f_back.f_code
fn.__code__.co_filename = fn.__code__.co_name = '&lt;string&gt;'
exec(compile(t, '&lt;string&gt;', 'exec'), fn.__code__.co_varnames, fn.__code__.co_varnames)
</code>

