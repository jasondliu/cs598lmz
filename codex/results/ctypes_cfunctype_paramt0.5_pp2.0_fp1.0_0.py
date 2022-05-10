import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class Callback(object):
    def __init__(self, callback):
        self.callback = FUNTYPE(callback)
    def __call__(self):
        self.callback()

def c_callback(*args):
    print('c callback')

callback = Callback(c_callback)

def run(callback):
    callback()

run(callback)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 19, in &lt;module&gt;
    run(callback)
  File "test.py", line 15, in run
    callback()
TypeError: 'CFUNCTYPE' object is not callable
</code>
I have no idea why this is happening. Any help would be appreciated.


A:

<code>self.callback</code> is a <code>CFUNCTYPE</code> object, not a callable.  You want to call it with <code>self.callback()</code>.  You also need to pass arguments to the callback
