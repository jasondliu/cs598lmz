import lzma
lzma.open("4.txt.xz")

#TypeError: initial_value must be str or None, not bytes
</code>
Any other way to read it?


A:

The accept_bytes parameter was removed from Python 3.6 and later.
You can use a context manager to read from the file.
<code>with lzma.open("4.txt.xz") as f:
    print(f.read().decode('utf-8'))
</code>

