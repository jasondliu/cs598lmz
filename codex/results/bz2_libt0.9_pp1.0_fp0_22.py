import bz2
bz2.compress(get.pan_reply)
</code>
when using python 2.4 , it will give me below  error message, 
error message:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute 'compress'
</code>


A:

This works for me in python 2.6:
<code>import bz2

response = "HTTP/1.1 200 OK\r\n\r\nThis is a test"

bz2.compress(response)
</code>
It is working in python 2.4:
<code>Python 2.4.3 (#1, May  2 2009, 23:44:21) 
[GCC 4.1.2 20070626 (Red Hat 4.1.2-13)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import bz2
&gt
