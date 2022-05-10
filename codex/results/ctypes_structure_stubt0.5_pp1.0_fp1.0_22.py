import ctypes

class S(ctypes.Structure):
    x = ctypes.c_bool

s = S()
s.x = True
print s.x
</code>
This works fine, but I want to be able to set the value to <code>1</code> or <code>0</code> as well. In the documentation it says that the <code>c_bool</code> type is an alias for <code>c_uint8</code>. So I tried to use <code>s.x = 1</code> but this gives me the following error:
<code>TypeError: integer assignment: a bytes-like object is required, not 'int'
</code>
I also tried <code>s.x = ctypes.c_uint8(1)</code> but that gives me the following error:
<code>TypeError: integer assignment: a bytes-like object is required, not '_ctypes.c_uint8'
</code>
Is there a way to set the value to <code>1</code> or <code>0</code>?


A:

The <code>c_bool</code> is a subclass of <code>
