import socket
socket.if_indextoname(1)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: an integer is required (got type str)
</code>
However, when I run the following code, it works fine:
<code>import socket
socket.if_indextoname('1')
</code>
The documentation for <code>if_indextoname</code> doesn't specify that the argument is a string.
Do I need to use the <code>int</code> function to convert the value to an integer, or is this a bug?
I am running:
<code>Linux version 2.6.32-431.el6.x86_64 (mockbuild@c6b9.bsys.dev.centos.org) (gcc version 4.4.7 20120313 (Red Hat 4.4.7-4) (GCC) ) #1 SMP Fri Nov 22 03:15:09 UTC 2013
</code>

