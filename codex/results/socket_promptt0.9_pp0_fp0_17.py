import socket
# Test socket.if_indextoname on AIX 6.1 with python 2.7 64 bits
# /opt/freeware/bin/python2.7-64 bit/python
# AIX ffsnw 5 6 00CDCCE3A3C0
print socket.if_indextoname(6)
</code>
I got a segmentation fault
<code>#0  0x090a861b in _socketmodule_getaddrcrit ()
#1  0x090d7451 in if_indextoname ()
#2  0x0000063d in ?? ()
#3  0x001042b0 in ?? ()
#4  0x0000054b in ?? ()
#5  0x00000268 in ?? ()
#6  0x000002a0 in ?? ()
#7  0x00101200 in ?? ()
#8  0x00101b1c in ?? ()
#9  0xffffffffffffffff in ?? ()
</code>
It seems related to the _socketmodule_getaddrcrit in _socketmodule.c. I'm using the standard python 2.7 64 bit /opt/freeware
