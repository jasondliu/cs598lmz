import socket
socket.if_indextoname(1)
</code>
returns:
<code>'wlan0'
</code>
How can I replicate this with ctypes?
Reference: C Struct: ifreq, Python socket Function: if_indextoname


A:

I finally figured this out. Here is a simplified version:
<code>from ctypes import *
from ctypes.util import find_library

class ifreq(Structure):
    _fields_ = [('ifr_ifrn', c_char * 16)
    ]

class sockaddr(Structure):
    _fields_ = [('sa_data', c_char * 14)
    ]

if __name__ == '__main__':
    libc_path = find_library('c')
    libc = cdll.LoadLibrary(libc_path)
    SIOCGIFNAME = 0x8910
    namebuf = create_string_buffer(16)
    sa = sockaddr(namebuf)
    ifr = ifreq(namebuf)
    ifr.ifr_ifindex = c_int(1)
