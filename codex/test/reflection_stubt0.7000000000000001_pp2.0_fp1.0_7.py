fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "<lambda>\n"

# The presence of the __closure__ attribute indicates a closure.
