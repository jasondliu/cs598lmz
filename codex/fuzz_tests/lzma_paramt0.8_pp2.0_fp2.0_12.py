from lzma import LZMADecompressor
LZMADecompressor
</code>
When I try to import the same on windows machine I get following error
<code>&gt;&gt;&gt; from lzma import LZMADecompressor
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Program Files\Python38\lib\lzma.py", line 9, in &lt;module&gt;
    from _lzma import *
ImportError: DLL load failed while importing _lzma: The specified module could not be found.
</code>
I have verified that python38.dll is present in the PATH.
Why I am getting the error.


A:

Maybe, you have to install <code>pyliblzma</code>
<code>pip install pyliblzma
</code>
See this link https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyliblzma

