import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    y = ctypes.c_uint8

s = S()
s.x = 0x10
s.y = 0x16
print 'read:', ctypes.c_uint16(s).value
s.x = 0x10
s.y = 0x16
print 'read:', ctypes.c_uint16(s).value
</code>
When tested on a 64-bit Python 2.6 on Windows 7 it prints <code>5136</code> as expected (0 appears to be assumed).  When run on a 64-bit Python 2.7 on Linux EL6 it prints <code>6630</code>.
Is this a bug in the Python 2.7 interpreter on Linux EL6 or am I not following the intepreter specification?  If I'm doing it right and it's a bug, is there a workaround?


A:

From looking at the source, it looks like the result is undefined behaviour.
The buffer should be zero-padded:
<code>memcpy(ptr[0], buf, bytes_needed);
memset(ptr[
