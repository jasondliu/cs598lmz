import lzma
lzma.open()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.4/lzma.py", line 6, in &lt;module&gt;
    import _lzma
ImportError: No module named '_lzma'
</code>
I'm running Ubuntu 14.04. I've installed the <code>liblzma-dev</code> package, but I still get the same error.


A:

The <code>lzma</code> module is not available on Ubuntu 14.04. It was added in Python 3.3, and Ubuntu 14.04 uses Python 3.4.
You can install Python 3.5 from the deadsnakes PPA to get the <code>lzma</code> module.

