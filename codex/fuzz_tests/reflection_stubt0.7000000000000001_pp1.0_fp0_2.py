fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'name'

print(fn.__code__)
print(fn.__name__)

#print(gi.gi_frame)
#print(gi.gi_running)
#print(gi.gi_code)
#print(gi.gi_frame.f_code)
#print(gi.gi_frame.f_code.co_name)
