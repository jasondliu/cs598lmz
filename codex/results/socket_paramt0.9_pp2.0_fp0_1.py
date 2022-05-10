import socket
socket.if_indextoname(1)
'lo0'
socket.if_nametoindex('eth0')
2
</code>
Using regular expressions:
<code>import re
re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', open('/proc/net/if_inet6').read())
['fe80::212:4b00:614b:3773', 'fe80::212:4b00:614b:38e5', 'fe80::a00:20ff:fe3b:5b58']
</code>
On the Python 2.6 interpreter, it returns: 
<code>['fe80::212:4b00:614b:3773%eth1', 'fe80::a00:20ff:fe3b:5b58%eth0', 'fe80::212:4b00:614b:38e5%eth1']
</code>
Both functions work well on Python 2.6.
Now, going to the many interfaces Python has, is there an API that can
