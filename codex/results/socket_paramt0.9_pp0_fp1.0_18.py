import socket
socket.if_indextoname('3')
</code>
However none of them worked. <code>ieee80211_ioctl_giwname</code> returned <code>en0</code>, which is for the WiFi interface in my network card with whitelisted access. But when I ran <code>ip link</code> there was no interface for that interface since it was not connected. Hence, does there exist a solution whereby I can get access to the name of an interface whose current status is <code>DOWN</code>?


A:

I ended up creating two scripts to solve my problem:
<code>interfaces_to_name.py</code>
<code>from ctypes import *
from ctypes.util import find_library
libc = cdll.LoadLibrary(find_library("c"))
c_uint32 = c_ulong

def if_indextoname(ifindex):
    "Return the name of the ifIndex interface."
    libc.if_indextoname.argtypes = (c_uint32, c_char_p)
    libc.if_indextoname.restype = c
