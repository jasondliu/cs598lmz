from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
And yet the first line generates a memory error. Why is this? How can I handle this?


A:

<code>BZ2Decompressor()</code> docs says
<blockquote>
<p>The BZ2Decompressor class provides an interface for incrementally
decompressing data that has been compressed using bzip2 compression.
The BZ2Decompressor class supports a incremental interface, with <strong>no need
to read all the data in one go.</strong></p>
</blockquote>
In you code, you are trying to read all the data in one go as you passed whole file to <code>BZ2Decompressor()</code>. Hence the error.
<code>with open('dblp-ref.xml.bz2', 'rb') as f, open('out', 'wb') as fout:
    decompressor = BZ2Decompressor()
    for data in iter(lambda : f.read(100 * 1024), b''):
        fout.write(decompressor.decompress(data))
</code>

