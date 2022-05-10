import lzma
lzma.open()
</code>
The error I get is:
<code>Traceback (most recent call last):
  File "C:\Users\micha\Desktop\test.py", line 5, in &lt;module&gt;
    lzma.open()
TypeError: open() missing 1 required positional argument: 'filename'
</code>
I am using Python 3.7.0 64-bit.
Thanks in advance for your help!


A:

You need to pass <code>lzma.open</code> a filename, as the error says.
<code>import lzma
lzma.open('/path/to/file.xz')
</code>

