from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open(filename, 'rb').read())

# or
BZ2Decompressor().decompress(open(filename, 'rb').read()).decode('utf-8')

# or
with bz2.BZ2File(filename, 'r') as f:
    data = f.read()

# or
with bz2.BZ2File(filename, 'r') as f:
    data = f.read().decode('utf-8')
</code>

