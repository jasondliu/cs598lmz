import lzma
# Test LZMADecompressor
COMPRESSED_DATA = b(
    "\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5"
    "\xa3\x01\x00\x04,\xa7\x01\x00\x00\x00\x00\xff\xff\xff\xff\x8a\xef"
    "\x16\x1b\xc2{b\x90\xa4\x90@\x00\x05I\x0c\x00\x00\x00Python\x00"
)
def test_get_lzma_decompress():
    assert lzma.LZMADecompressor().decompress(COMPRESSED_DATA) == b("Hello")

def test_timestamp_in_filename():
    from sphinxcontrib.paverutils import _log, _timestamp_in_filename
    test_dict, test_base_fn =
