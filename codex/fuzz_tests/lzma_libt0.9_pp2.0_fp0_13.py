import lzma
lzma.LZMAFile([spec])
</code>
Tryin to open .xz file with LZMAFile. But i got this error "TypeError: expected integer or long"
How to solve this problem?
Or is there any other way to open .xz file in python?
Thank you.


A:

<code>lzma.LZMAFile</code> is capable of handling shortcuts to LZMA files, but only when they are a string containing the filename.
If you want to pass a different kind of file object, use <code>lzma.open</code>.
<code>with lzma.open(spec) as fileobj:
    print(fileobj.read())
</code>

