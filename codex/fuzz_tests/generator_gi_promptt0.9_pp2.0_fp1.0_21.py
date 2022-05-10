gi = (i for i in ())
# Test gi.gi_code.
gi.gi_code.co_filename in ("(generator)", "<stdin>")
gi.gi_code.co_firstlineno == 1

# Test gi.gi_frame.
f.f_code == gi.gi_frame.f_code
gi.gi_frame.f_back == f

# Test gi.gi_frame attribute setter
def f(): pass
def gf(): yield None
f_frame = f.__code__.co_firstlineno
gf_frame = gf().gi_frame
f_frame == gf_frame
try:
    f_frame.f_code = gf.__code__
except AttributeError:
    pass
else:
    print("f.gi_frame.f_code setter doesn't raise AttributeError")
