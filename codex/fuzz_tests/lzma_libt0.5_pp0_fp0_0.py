import lzma
lzma.decompress(data)
</code>
Btw, the error message is misleading. It's not the <code>lzma</code> module that doesn't have a <code>decompress</code> attribute, it's the <code>lzma</code> module's <code>compressobj</code> class that doesn't have a <code>decompress</code> attribute.

