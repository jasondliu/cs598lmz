gi = (i for i in ())
# Test gi.gi_code


def f():
    pass

gi.gi_code = f.func_code
try:
    next(gi)
except ValueError:
    pass
else:
    raise AssertionError

# Test gi.gi_frame

gi.gi_code = f.func_code
gi.gi_frame = f.func_traceback
try:
    next(gi)
except ValueError:
    pass
else:
    raise AssertionError

# Test gi.gi_frame (frame is not eval_frame)

def f():
    try:
        g()
    except:
        x = sys.exc_info()[2].tb_frame.f_back
    return x

def g():
    1 / 0
gi.gi_code = f.func_code
gi.gi_frame = f.func_traceback
next(gi)
gi.gi_frame = x
try:
    next(gi)
except ValueError:
    pass
else:
    raise AssertionError

# Test gi.gi_
