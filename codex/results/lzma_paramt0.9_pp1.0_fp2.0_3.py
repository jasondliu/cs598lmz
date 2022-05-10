from lzma import LZMADecompressor
LZMADecompressor().decompress(buff)
</code>
because of the uncaught limit, I assume. I'd rather not catch it for some reason or another, so... is there a rationale for this limit not being adjustable? Is there a different alternative (although in my case <code>LZMAStream</code> *should *do it...) that I should resort to?

