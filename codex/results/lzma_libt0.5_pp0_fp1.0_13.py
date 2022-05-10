import lzma
lzma.open
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute 'open'
</code>
I have installed pyliblzma. 
What am I doing wrong?
EDIT:
I am using Python 2.7.6 on CentOS 6.5


A:

<code>lzma</code> is a built-in module in Python 3.3 and later. It's not available in Python 2.7.
You need to use the <code>pyliblzma</code> module, which provides a backport of the Python 3.3 <code>lzma</code> module to Python 2.

