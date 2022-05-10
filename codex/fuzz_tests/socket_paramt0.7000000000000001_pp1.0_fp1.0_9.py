import socket
socket.if_indextoname(index)
</code>
But for some reason I only get the first few of my interfaces.  What's going on? 
I'm on Mac OS X 10.6.8.


A:

It is a known bug in Mac OS X:
https://bugs.python.org/issue17999
<code>$ python
Python 2.7.6 (default, Sep  9 2014, 15:04:36) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import socket
&gt;&gt;&gt; socket.if_indextoname(16)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "socket.py", line 428, in if_indextoname
    return _testcapi.if_indextoname(ifname, index)

