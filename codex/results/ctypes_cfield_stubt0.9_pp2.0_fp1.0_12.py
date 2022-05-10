import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(S):
    _fields_ = [('y', S.x)]

    def copy(self):
        new = D()
        for i in range(len(self._fields_)):
            setattr(new, self._fields_[i][0],
                    getattr(self, self._fields_[i][0]))
        return new
</code>
Then call it:
<code>&gt;&gt;&gt; s = D(x=3, y=4)
&gt;&gt;&gt; s.copy()
(3, 4)
</code>
Of course, this is not very robust and there are probably many edge cases that break it. If you want to be more careful and make this work with structures that are created by yourself, then you could do:
<code>import ctypes
from copy import copy

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(S):
    _fields_ = [('y', S.x)]

    def copy(self
