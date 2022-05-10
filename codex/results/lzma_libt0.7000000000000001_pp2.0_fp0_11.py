import lzma
lzma.open('file.xz')
</code>
or
<code>import lzma
with lzma.open('file.xz') as f:
    contents = f.read()
</code>

