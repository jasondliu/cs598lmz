import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()

for i in xrange(100000):
    s.x += 1
    s.y += 1
    s.z += 1
</code>
This runs about twice as long as the original, but the box is still only using one core.  I'm not sure what else to try.
EDIT:
I'm running this on a Ubuntu 10.4.1 box with python 2.6.5.  I have a dual core box.
EDIT2:
The output from <code>taskset -p 0 $!</code> is:
<code>pid 14626's current affinity list: 1
pid 14626's new affinity list: 0
</code>
EDIT 3:
I'm running the code on a VM.  The output of <code>lscpu</code> is:
<code>Architecture:          i686
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                2

