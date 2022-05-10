import ctypes
# Test ctypes.CFUNCTYPE on a simple python function
#
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char)
def add2(ch):
    return ord(ch) + 2

print (add2('A'))
</code>
I am getting an error:
<code>Traceback (most recent call last):
File "type.py", line 9, in &lt;module&gt;
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char)
TypeError: 'CFUNCTYPE' object is not callable
</code>

