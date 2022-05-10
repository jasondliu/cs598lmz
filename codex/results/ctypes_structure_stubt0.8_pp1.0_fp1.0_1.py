import ctypes

class S(ctypes.Structure):
    x = 42
    def __init__(self):
        self._b = False

    @property
    def b(self):
        self._b = not self._b
        return self._b

a = S()
print(a.x)
print(a.b)
print(a.x)
print(a.b)
</code>
prints
<code>42
True
42
False
</code>

