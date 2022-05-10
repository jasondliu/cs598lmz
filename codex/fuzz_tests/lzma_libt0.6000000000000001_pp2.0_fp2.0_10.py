import lzma
lzma.open
</code>
And the error message:
<code>Traceback (most recent call last):
  File "C:\Users\myName\Desktop\Python\lzma.py", line 1, in &lt;module&gt;
    import lzma
  File "C:\Users\myName\Desktop\Python\lzma.py", line 2, in &lt;module&gt;
    lzma.open
AttributeError: module 'lzma' has no attribute 'open'
</code>


A:

The problem is that you have a file called <code>lzma.py</code> in the same directory as your script. Python is finding that file first, before your <code>lzma</code> package.
Rename your file to something else and try again.

