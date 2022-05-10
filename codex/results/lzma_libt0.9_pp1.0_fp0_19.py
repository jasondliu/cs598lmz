import lzma
lzma.compress(b'hello')
</code>
<blockquote>
<p><code>&lt;code&gt;File "&amp;lt;ipython-input-27-85627f66275c&amp;gt;", line 1, in &amp;lt;module&amp;gt;&lt;br/&gt;
  lzma.compress(b'hello')&lt;br/&gt;
  AttributeError: module 'lzma' has no attribute 'compress'&lt;/code&gt;</code></p>
</blockquote>
I also tried adding this to the top of my script but it still didn't work:
<code>import sys
!{sys.executable} -m pip install lzma
</code>
How do I install the <code>lzma</code> library? I would also like to use this in Heroku later as well.

