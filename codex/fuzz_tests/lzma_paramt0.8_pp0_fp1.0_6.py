from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# mypy doesn't allow this though.
def decompress_lzma(data: bytes) -&gt; bytes:
    return LZMADecompressor().decompress(data)
</code>
This is because the <code>bytes</code> type is not a Container[AnyStr].
Any ideas how I can work around this?


A:

I don't believe you can.  The <code>bytes</code> type has no information associated with it other than its length.  It's not like the <code>Iterable</code> type, for instance, which knows that each contained item can be iterated over.
In fact, <code>bytes</code> is explicitly not a subtype of <code>Container</code> as you can see from this mypy source line.

