import lzma
lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
</code>
I get:
<blockquote>
<p>DeprecationWarning: Using or importing the ABCs from 'collections' instead
  of from 'collections.abc' is deprecated, and in 3.8 it will stop working</p>
</blockquote>
The warning is coming from the <code>python3-lzma</code> package. 
This is the output on Python 3.7.1:
<code>$ python
Python 3.7.1 (default, Dec 14 2018, 19:28:38) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import lzma
&gt;&gt;&gt; lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
__main__:1: DeprecationWarning: Using or importing the ABCs from 'collections'
