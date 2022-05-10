import bz2
bz2.BZ2Compressor()
</code>
The actual error I get is as follows
<blockquote>
<p>Traceback (most recent call last):   File
  "/home/zeno/.local/lib/python3.6/site-packages/attrs/__init__.py",
  line 222, in <strong>getattr</strong>
      return getattr(self.<strong>obj</strong>, name) AttributeError: 'BZ2Compressor' object has no attribute '_is_streame
  d'</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):   File "/usr/lib/python3.6/bz2.py",
  line 117, in <strong>new</strong>
      return bz2.BZ2Compressor(*args, **kwargs) TypeError: object.__new__() takes no parameters</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):
