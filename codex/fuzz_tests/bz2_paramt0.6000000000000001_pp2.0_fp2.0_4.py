from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
</code>
If you want to do it in the context of a file, you can use <code>BZ2File</code> objects.
<code>&gt;&gt;&gt; from bz2 import BZ2File
&gt;&gt;&gt; with BZ2File("test.txt.bz2", "r") as f:
...     f.read()
...
'This is the test file\n'
</code>

