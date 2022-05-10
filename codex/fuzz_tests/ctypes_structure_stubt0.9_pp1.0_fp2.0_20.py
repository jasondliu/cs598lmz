import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int32

import clr
clr.AddReference('System.Runtime.InteropServices')
from System.Runtime.InteropServices import Marshal

buf = Marshal.AllocHGlobal(10000)

Marshal.WriteInt32(buf, 0, 1)
Marshal.WriteInt32(buf, 4, 2)

s = ctypes.cast(buf, ctypes.POINTER(S))
print s.contents.x
print s.contents.y

Marshal.FreeHGlobal(buf)
</code>
Output:
<code>1
2
</code>

