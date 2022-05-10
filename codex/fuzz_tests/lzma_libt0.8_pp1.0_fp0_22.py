import lzma
lzma.open
</code>
here i got the error message as shown below
<code>&gt;&gt;&gt; lzma.open
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
NameError: name 'lzma' is not defined
</code>


A:

You probably installed the xz-based <code>lzma</code> module.  It's not the same as the <code>lzma</code> module from the <code>backports.lzma</code> package which is compatible with the standard library.

