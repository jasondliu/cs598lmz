import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

print(S())

S.x = 3

print(S())
</code>
outputs:
<code>&lt;__main__.S object at 0x10f83afb0&gt;
&lt;__main__.S object at 0x10f83afb0&gt;
</code>
I'd like the first print to be:
<code>&lt;__main__.S object at 0x10f83afb0 x=0&gt;
</code>


A:

<code>class S(ctypes.Structure):
    def __init__(self):
        super().__init__()
        self.x = ctypes.c_int()
</code>

