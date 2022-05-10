import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f():
    return S()

print(f())
</code>
This will print <code>&lt;__main__.S object at 0x7f2d0f0b9f28&gt;</code>, which is a lot more useful than just <code>0x7f2d0f0b9f28</code>.

