import lzma
lzma.LZMACompressor
</code>
The output is the following:
<code>---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
&lt;ipython-input-4-e69dd0c7a415&gt; in &lt;module&gt;()
----&gt; 1 import lzma
      2 lzma.LZMACompressor

AttributeError: 'module' object has no attribute 'LZMACompressor'
</code>
Also, I tried the following code:
<code>import bz2
import zlib
import lzma
</code>
The output is the following:
<code>---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
&lt;ipython-input-5-0cdda6a2b2e0&gt; in &lt;module&gt;()
      1 import bz2
      2 import zlib
----&gt; 3 import lzma
      4 
      5 print(bz2.BZ2Compressor())

AttributeError: 'module' object has
