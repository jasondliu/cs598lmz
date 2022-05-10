import lzma
lzma.open(filepath, "rb")
</code>
The reason for this is that the <code>lzma</code> module only supports xz format, not 7z.

