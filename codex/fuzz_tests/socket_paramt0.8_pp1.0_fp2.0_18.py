import socket
socket.if_indextoname(3)

'en0'
</code>
but if I do this
<code>&gt;&gt;&gt; socket.if_indextoname(8)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
OSError: [Errno 19] No such device
</code>
This happens on 10.6, but not 10.5.  All the forum posts I've seen about this seem to point to a problem with the /System/Library/Extensions/IONetworkingFamily.kext and suggest replacing it with a copy from 10.5, but I've seen no evidence that this actually works.  When I do this, I'm able to get the kernel extension to load again, but the if_indextoname call still fails.
Does anyone know of a workaround or fix?


A:

So, this is a bug in the kernel extensions.  The data structure that it uses to store things is different in 10.6 than in 10.5 and can sometimes overflow.  It's not known exactly how to reproduce
