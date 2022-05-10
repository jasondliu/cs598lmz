import ctypes
# Test ctypes.CField implementation

lib = ctypes.CDLL(ctypes.util.find_library('m'))

class strncmp(ctypes.Structure):
    _fields_ = [('PCC', ctypes.c_char_p), ('PCC', ctypes.c_char_p), ('SS', ctypes.c_int)]

if __name__ == '__main__':
    strcmp = lib.strncmp
    print(strcmp)
    strcmp.argtypes = (ctypes.POINTER(strncmp), ctypes.POINTER(strncmp))
    strcmp.restype = ctypes.POINTER(strncmp)

    print(strncmp)
    print(strncmp(PCC='Hello', SS=7))
</code>
This is the error I got:
<code>Traceback (most recent call last):   File "test.py", line 13, in &lt;module&gt;
    print(strncmp(PCC='Hello', SS=7))   File "/usr/lib/python2.7/ctypes/__
