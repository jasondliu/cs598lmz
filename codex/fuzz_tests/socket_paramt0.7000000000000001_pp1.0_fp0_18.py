import socket
socket.if_indextoname(1)

In [6]: socket.if_indextoname(1)
Out[6]: 'eth0'

In [7]: socket.if_indextoname(2)
Out[7]: 'eth1'

In [8]: socket.if_indextoname(3)
---------------------------------------------------------------------------
error: (99, 'Cannot assign requested address')


In [9]: socket.if_nameindex()
Out[9]: [(1, 'eth0'), (2, 'eth1')]
</code>
I'm not sure how interface indices are assigned. I thought they were assigned in order they were brought up. 
So I try to bring down eth0 and see what happens:
<code>In [10]: subprocess.call(["sudo", "ifconfig", "eth0", "down"])
0

In [11]: socket.if_nameindex()
Out[11]: [(2, 'eth1'), (1, 'eth0')]

In [12]: socket.if_indextoname(1)
---------------------------------------------------------------------------
error: (99, 'Cannot assign
