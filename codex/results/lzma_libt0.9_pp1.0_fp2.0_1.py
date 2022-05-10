import lzma
lzma.open(path)
</code>
and it appears that lzma does support files that are missing the end CRC checksum.
How exactly does lzma do this?
I'm considering using this behaviour as an alternative to filehole, as it's a small price to pay not to worry about the end-of-file CRC corrupting my own application's data at the end of the file.  However, I would only do it this way if I could be sure the lzma approach is reliable.

