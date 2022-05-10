import lzma
lzma.LZMAFile('foo.xz')
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "foo.py", line 1, in &lt;module&gt;
    import lzma
  File "C:\Python27\lib\lzma.py", line 5, in &lt;module&gt;
    from _lzma import *
ImportError: DLL load failed: The specified module could not be found.
</code>
I'm using Python 2.7 under Windows 7 32bit.


A:

On Windows, you need to install the <code>pyliblzma</code> file (also known as <code>pylzma</code>) for your version of Python. Unfortunately it isn't distributed with Python. The easiest way to install it is to use <code>pip</code>, like so:
<code>C:\python27\Scripts\pip.exe install pyliblzma
</code>
This downloads and installs the relevant dependencies into <code>C:\python27\Scripts\Lib</
