import socket
socket.if_indextoname(150))
</code>
I get an error in python2:
<code>socket.error: (19, 'No such device')
</code>
I get an error in python3:
<code>IndexError: list index out of range
</code>
on my laptop (which also has Linux Mint).  I can see the interface name with <code>sudo ip link</code> or <code>ifconfig</code> but I don't know how to get the index from that.


A:

You need to look at <code>/sys/class/net</code>:
<code>In [1]: import sys

In [2]: import socket

In [3]: for i in os.listdir('/sys/class/net'):
   ...:     if i != 'lo':
   ...:         print(i, int(os.readlink('/sys/class/net/' + i).split('/')[-1][3:]))
   ...:
eno1 2
</code>

