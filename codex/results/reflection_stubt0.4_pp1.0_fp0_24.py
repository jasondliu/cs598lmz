fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #13184: segfault when an exception is raised in the __del__
# method of a traceback object.
import sys
class C(object):
    def __del__(self):
        raise Exception
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    tb.tb_frame.f_locals['c'] = C()
    del tb

# Issue #13186: segfault when an exception is raised in the __del__
# method of a frame object.
import sys
class C(object):
    def __del__(self):
        raise Exception
try:
    raise Exception
except:
    f = sys.exc_info()[2].tb_frame.f_back
    f.f_locals['c'] = C()
    del f

# Issue #13187: segfault when an exception is raised in the __del__
# method of a traceback object.
import sys
class C(object):
    def
