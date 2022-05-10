import lzma
lzma.open(filename)
</code>
This works fine for normal files, but it does not work for files that have been compressed with <code>gzip</code>.
<code>import gzip
gzip.open(filename)
</code>
This works fine for normal files, but it does not work for files that have been compressed with <code>lzma</code>.
I have tried to detect the compression of the file by checking the first few bytes, but this is not reliable.
<code>def get_compression(filename):
    with open(filename, 'rb') as f:
        magic = f.read(3)
        if magic == b'\x1f\x8b\x08':
            return 'gzip'
        elif magic == b'\xfd7zXZ\x00':
            return 'lzma'
        else:
            return None
</code>
How can I open a file that was compressed with either <code>lzma</code> or <code>gzip</code>?


A:

You can use the <code>file
