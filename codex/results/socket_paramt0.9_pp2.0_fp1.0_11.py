import socket
socket.if_indextoname('3')
</code>
It returns <code>eth0</code> instead of <code>eth0:0</code>.
Is there a way I can get <code>eth0:0</code> programmatically?


A:

In case you had in mind to get a list of all the interfaces, you can use:
<code>import netifaces as ni
print(ni.interfaces())
</code>
which will return:
<code>['lo0', 'gif0', 'stf0', 'XHC0', 'XHC20', 'en0', 'en1', 'fw0', 'p2p0']
</code>

