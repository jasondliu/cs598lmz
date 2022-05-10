fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    assert fn(), 'Function assumes that code object is callable'
except TypeError as e:
    assert 'not callable' in str(e), 'Wrong exception'
else:
    assert False, 'Wrong exception'

fn = lambda: None
gi = (i for i in ())
gi.gi_frame = None
fn.__code__ = gi
try:
    assert fn(), 'Function assumes that code object has frame'
except TypeError as e:
    assert 'no frame' in str(e), 'Wrong exception'
else:
    assert False, 'Wrong exception'

# This is not on Python 2
# fn = lambda: None
# gi = (i for i in ())
# gi.gi_frame = ()
# fn.__code__ = gi
# try:
#     assert fn(), 'Function assumes that code object has attached frame'
# except TypeError as e:
#     assert 'frame is wrong' in str(e), 'Wrong exception'
# else:
#     assert False, 'Wrong exception'

