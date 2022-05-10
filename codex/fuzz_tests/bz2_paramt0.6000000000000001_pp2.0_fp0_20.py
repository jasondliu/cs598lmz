from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
I get this error:
<code>TypeError: __init__() takes at least 2 arguments (1 given)
</code>
I am using Python 2.7.11.
What's going on?


A:

It's because you're using Python 2, not Python 3.
In Python 2, you need to pass in a string representing the data you want to decompress:
<code>BZ2Decompressor(data)
</code>
In Python 3, you can just call the constructor normally and then use the <code>decompress()</code> method:
<code>dc = BZ2Decompressor()
dc.decompress(data)
</code>

