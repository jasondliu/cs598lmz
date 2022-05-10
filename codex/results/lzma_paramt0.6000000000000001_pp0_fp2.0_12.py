from lzma import LZMADecompressor
LZMADecompressor().decompress(b)
</code>
I'd like to be able to use the <code>LZMADecompressor</code> class directly, but it seems to be missing the <code>decompress</code> method.
<code>&gt;&gt;&gt; import lzma
&gt;&gt;&gt; dir(lzma.LZMADecompressor())
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_buffer', '_decompressor', '_eof
