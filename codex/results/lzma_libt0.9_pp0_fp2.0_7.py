import lzma
lzma.decompress('')
print(lzma)
</code>


A:

Is this as simple as:
<code>import lzma
lzma.decompress(b"")
print(lzma)
</code>
the input is expected to be a <code>bytes</code> object, not a string.

