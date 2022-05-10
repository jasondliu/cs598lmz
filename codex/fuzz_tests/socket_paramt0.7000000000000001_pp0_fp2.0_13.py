import socket
socket.if_indextoname(3)

# import socket
# socket.if_indextoname(3)
# 'en0'
</code>
which is my (wireless) ethernet card.
So I guess either
<code>sudo ifconfig en0 10.37.129.2
</code>
or 
<code>sudo ifconfig en1 10.37.129.2
</code>
should work for you.

