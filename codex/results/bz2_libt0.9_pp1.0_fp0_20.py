import bz2
bz2.compress('@yahoo.com',9)
</code>
and I got the following error:
<code>Traceback (most recent call last):
  File "C:/Python27/test.py", line 2, in &lt;module&gt;
    bz2.compress('@yahoo.com',9)
TypeError: must be string or buffer, not int
</code>


A:

You are using the wrong function. You want <code>decompress()</code>, not <code>compress()</code>:
<code>&gt;&gt;&gt; import bz2
&gt;&gt;&gt; bz2.decompress(b'BZh91AY&amp;SYA\xc4\xaf\xe5\x8f{G\xbe\x9dN')
'@yahoo.com'
</code>
The <code>compress()</code> function only compresses data; you have to call <code>decompress()</code> to get it back.
The <code>compress()</code
