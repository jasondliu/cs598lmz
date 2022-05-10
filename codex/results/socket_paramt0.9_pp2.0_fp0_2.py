import socket
socket.if_indextoname(3)
'lo0'
</code>
I am running OSX Lion, and my main interface is a built-in Thunderbolt Ethernet port.
Is it a bug/misconfiguration? Is it some kind of exotic case that is not officially supported?


A:

The problem is that by default, in Mavericks and Yosemite, <code>if_indextoname</code> is implemented in terms of a system call, <code>ifnet_namefromindex</code>.  And, by default, it only reports data interfaces, not the loopback interface.  Following this route, you get:
<code>$ python
Python 2.7.9 (default, Jul  2 2015, 01:26:46) 
[GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.49)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import sys, socket
&gt;&gt;&gt; sys.platform
'darwin'
&gt;&gt;&gt
