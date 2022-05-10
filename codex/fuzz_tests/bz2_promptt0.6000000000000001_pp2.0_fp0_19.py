import bz2
# Test BZ2Decompressor
with bz2.BZ2File(path, 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(block)
        if data:
            print(data)

import bz2
# Test decompress()
with bz2.BZ2File(path, 'rb') as f:
    for block in iter(lambda: f.read(100 * 1024), b''):
        data = bz2.decompress(block)
        if data:
            print(data)
</code>
I think the problem is the last two lines of the file are missing, so I tried <code>f.seek(-2, 2)</code> and <code>f.seek(2, -1)</code> but both don't work.
What can I do to make the last two lines appear?


A:

I don't think it's the last two lines that are missing.  The last two lines are just truncated. 
