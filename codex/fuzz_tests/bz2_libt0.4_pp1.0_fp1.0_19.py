import bz2
bz2.decompress(file)
</code>
I get the error message:
<code>ValueError: invalid start byte
</code>
I've checked the file and it is definitely a bz2 file.
I've tried using the <code>bz2.BZ2File</code> class but I can't get that to work either.
Any suggestions?


A:

<code>bz2.decompress()</code> expects a string, not a file object.
<code>bz2.BZ2File</code> is a file-like object that you can read from to get the uncompressed data.
<code>with bz2.BZ2File(file_name) as f:
    data = f.read()
</code>

