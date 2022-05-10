fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_code = fn
gi.gi_frame = {'f_locals': {gi:gi}}

gi.gi_code.gi_code = gi

fn.__closure__ = (gi,)
gi.gi_frame.f_locals.keys()

fn.__code__.co_flags = 0x2000

del fn
del gi
print "testing "

# i686-w64-mingw32-gdb.exe -ex "run" -ex "where" -ex "bt" -ex "quit" generator_injection.py
