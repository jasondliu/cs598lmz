import lzma
lzma.open(sys.argv[1], 'r')
</code>
If I do it in the terminal, it works:
<code>(Python3) oli@mint ~ $ python3
Python 3.8.2 (default, Mar 26 2020, 15:53:00) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import lzma
&gt;&gt;&gt; lzma.open('/home/oli/Downloads/test.xz', 'r')
&lt;lzma.LZMAFileReader object at 0x7f6ac814a750&gt;
</code>
Yet, in my python script:
<code>Traceback (most recent call last):
  File "./test.py", line 3, in &lt;module&gt;
    lzma.open(sys.argv[1], 'r')
  File "/home/oli/.local/lib/python3.8/site-
