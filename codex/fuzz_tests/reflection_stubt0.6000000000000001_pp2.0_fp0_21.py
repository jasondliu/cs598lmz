fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__closure__ = gi.gi_frame.f_locals.get('x')

print(fn.__closure__)
print(fn())
