import socket
socket.if_indextoname(1)

</code>


A:

No need to check if it's an IPv6 or IPv4 address:
<blockquote>
<p>Python supports both IPv4 and IPv6, and some APIs do not care about
  the version <strong>(for example, you can pass either an IPv4 or an IPv6
  address to the socket.connect() API)</strong>.</p>
</blockquote>
You can use <code>socket.gethostbyname</code> in your case.

