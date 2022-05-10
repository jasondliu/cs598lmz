import socket
socket.if_indextoname("1")
</code>
Only answers I find are through C, C#, and not python.
(I was able to solve the problem myself, will accept my answer myself)


A:

You can rely on this library:
https://github.com/phihag/pyroute2/
The command:
<code>from pyroute2 import IPRoute
ip = IPRoute()
print [ip.link_lookup(ifname='eth1')[0]]
</code>
will print the result you need. For instance, for me it said:
<code>[3]
</code>
So looks like <code>eth1</code> is the <code>3rd</code> network interface of my machine.

