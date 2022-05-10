gi = (i for i in ())
# Test gi.gi_code


# Test stop_immediately

import signal, os
save = signal.signal(signal.SIGINT, signal.SIG_IGN)
try:
    os.kill(os.getpid(), signal.SIGINT)
finally:
    signal.signal(signal.SIGINT, save)

# Test _set_tstate_lock()

class MyException(Exception):
    pass

def bogus_pyframe_dealloc(pyframe):
    raise MyException

import sys
bogus_pyframe_dealloc._dont_inline_ = True   # Prevent inline of simple function

def test_pyframe_dealloc():
    save = sys._pyframe_dealloc
    try:
        sys._pyframe_dealloc = bogus_pyframe_dealloc
        try:
            raise ValueError
        except ValueError:
            pass
    finally:
        sys._pyframe_dealloc = save

test_pyframe_dealloc()

class B(object):
  def __init__(self):
    self.b =
