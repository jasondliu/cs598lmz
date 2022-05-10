import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

del ctypes, S
</code>
The module <code>test.py</code> is almost identical:
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

del ctypes, S
</code>
It has the same effect on <code>ctypes</code> to add the attribute <code>CField</code>, but contains no <code>imports</code> other than <code>ctypes</code>.
In my <code>AWS Lambda</code> function, where I'm trying to use this module, it works just fine if I import <code>test</code>, but fails with the <code>TypeError</code> in the title if I import <code>one</code>. For instance, if I change:
<code>import ctypes
import one
</code>
To
<code>import ctypes
import test
</code>
Everything works as expected.
I need to understand what is going on in this case, but
