import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [
        ("y", ctypes.c_char_p),
        ("z", ctypes.c_void_p),
        ("u", ctypes.c_ulong),
    ]

S()
</code>


A:

This is because your <code>S</code> class is a subclass of <code>ctypes.Structure</code> and the <code>ctypes.Structure</code> initialiser takes a <code>i_w_s</code> argument which is an instance of the <code>_CData_Internal</code> class that is created when you call the constructor on an instance of <code>ctypes.Structure</code>.
If you change the class to this, the <code>__init__</code> function should work:
<code>class S(ctypes.Structure):
    _fields_ = [
        ("y", ctypes.c_char_p),
        ("z", ctypes.c_void_p),
        ("u", ctypes.c_ulong),
    ]

    def __init
