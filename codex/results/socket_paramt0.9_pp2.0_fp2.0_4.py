import socket
socket.if_indextoname(2)

'ens160'

socket.if_nametoindex('ens160')

24
</code>
I can't really figure out what is the difference and since socket doesn't give any change log I would really appreciate to explain how can I move to the function <code>if_indextoname()</code>


A:

You need to pass an integer, not a string.  Convert your string <code>'2'</code> to an integer with <code>int()</code>.

