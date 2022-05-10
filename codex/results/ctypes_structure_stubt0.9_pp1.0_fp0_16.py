import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint()
    y = ctypes.c_uint()

class R(ctypes.Structure):
    _fields_ = [("x",ctypes.c_uint),("y",ctypes.c_uint)]
    def __lt__(self,y):
        if self.x &lt; y.x:
            return True
        if self.x &gt; y.x:
            return False
        if self.y &lt; y.y:
            return True
        if self.y &gt; y.y:
            return False
        return False
</code>
Then I compare using:
<code> R(11, 52) &lt; R(130, 40)
</code>
I've also tried:
<code>@functools.total_ordering
class R(ctypes.Structure):
    _fields_ = [("x",ctypes.c_uint),("y",ctypes.c_uint)]
    def __le__(self,y):
        if self.x &lt; y.x:
            return True
