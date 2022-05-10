import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hi'

assert isinstance(fun(), str)

class A(ctypes.Structure):
    _fields_ = [("fun", FUNTYPE)]
a = A(fun)
assert isinstance(a.fun(), str)

import pickle
pickle.dumps(a.fun)
</code>

dump
<code>ctypes.Structure</code> does not have a <code>__reduce__</code> method so I get a protocol error from <code>pickle.dumps(a)</code>
Using <code>pickle.HIGHEST_PROTOCOL</code> does not help
Using <code>cloudpickle.dumps</code> does not help
using <code>dill.dumps</code> fails
Using <code>pickle</code> source code, I can dump <code>a</code> successfully
<code>import pickle
import pickle
from pickletools import dis

args = (A,(fun,))
dis(pickle.dumps(args))
</code>
output
<code>   
