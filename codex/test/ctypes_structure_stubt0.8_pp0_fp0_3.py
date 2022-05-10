import ctypes

class S(ctypes.Structure):
    x = 0
    y = 0

a = S()
print(a)
# &lt;__main__.S object at 0x0000000002E1B908&gt;
