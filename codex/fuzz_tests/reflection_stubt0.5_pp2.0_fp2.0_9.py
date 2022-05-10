fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# The following should not crash
import _testcapi
_testcapi.with_tp_del()
_testcapi.with_del()
_testcapi.with_del_through_gc()

# Issue #13333: Don't crash when the current frame is NULL.
def f():
    _testcapi.raise_exception(1)

def g():
    try:
        f()
    except:
        _testcapi.raise_null_frame()

try:
    g()
except TypeError:
    pass

# Issue #14056: don't crash when the current frame is NULL.
# This test is the same as the previous one, but raises the exception
# from a different thread.
import threading
def f():
    _testcapi.raise_exception(1)

def g():
    try:
        f()
    except:
        _testcapi.raise_null_frame()

def h():
    threading.Thread(target=g).start()


