import lzma
# Test LZMADecompressor.format_error, including
# decompressor.decompress(b'', max_length=-1)

for msg in (None,
            "",
            "foo",
            "foo\nbar",
            "foo\nbar\nbaz",
            "foo\nbar\nbaz\nquux"):
    with pytest.raises(lzma.LZMAError, match=msg):
        lzma.LZMADecompressor().format_error(msg)

with pytest.raises(lzma.LZMAError, match=r'^\Z'):
    lzma.LZMADecompressor().format_error(None)

with pytest.raises(lzma.LZMAError, match=r'^foo$'):
    lzma.LZMADecompressor().format_error("foo")

with pytest.raises(lzma.LZMAError, match=r'^foo:\n bar$'):
    lzma.LZMADecompressor().
