import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(42)
    y = ctypes.c_float(123)
    def __init__(self):
        print "init called"
        ctypes.Structure.__init__(self)
        print "init done"

s = S()
print "values", s.x, s.y
</code>
Output:
<code>init called
init done
values 42.0 123.0
</code>

