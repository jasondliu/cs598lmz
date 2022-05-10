import socket
socket.if_indextoname(3)
</code>
Why is the result of both commands different?


A:

<blockquote>
<p>Unlike the if_nameindex() function, this function may or may not
  include certain interfaces. Some operating systems support
  configuration of interfaces which exist, but are not currently
  operational or are not configured to an IP address. These interfaces
  may be omitted for security reasons, or because they are not
  available for use.</p>
<p>If the interface with the given index does not exist,
  if_indextoname() returns a null pointer.</p>
</blockquote>

