from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
The reason for the error is that the LZMA format (which is used by the popular <code>xz</code> utility) is a multi-stream format, but the <code>lzma</code> module only supports single-streams.

