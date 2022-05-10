fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = gi.gi_frame.f_code
gi.gi_frame.f_code = fn
</code>
This is a pretty ugly hack, but it works.

