import lzma
lzma.open
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute 'open'
</code>
I'm not sure why this is happening. I'm using Python 2.7.3.


A:

<code>lzma</code> is a backport of the Python 3.3 <code>lzma</code> module. It is not a part of the standard library, you need to install it separately.

