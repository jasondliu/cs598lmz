import ctypes

class S(ctypes.Structure):
    x = 0
    y = 0

a = S()
print(a)
# &lt;__main__.S object at 0x0000000002E1B908&gt;
</code>
How to do that using the <code>__new__</code> method?


A:

Add a <code>__init__</code> after you create your custom type:
<code>DummyStructure = type("DummyStructure", (ctypes.Structure,), {})

def __init__(self, x, y):
    self.x = x
    self.y = y

DummyStructure.__init__ = __init__
</code>

