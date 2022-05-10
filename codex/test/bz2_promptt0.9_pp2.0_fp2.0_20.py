import bz2
# Test BZ2Decompressor/compressFile
expected = '''123
abc
&*.
'''

def test_bz2_decompress():
    """This is a regression test for a bug prior to 2.6.  The bug was that
    utf-8-encoded input was decompressed incorrectly when text was mixed with
    binary data.
    """
    if sys.version_info < (2, 6):
        pytest.skip("Test valid for Python 2.6+")
    data = 'BZh91AY&SYx'
    out_data = bz2.BZ2Decompressor().decompress(data)
    assert out_data == expected

def test_bz2_compress():
    """This is a regression test for a bug prior to 2.6.  The bug was that
    bz2.compressFile would output the wrong amount of data unless mode="w"
    or mode="wb" was used.
    """
    if sys.version_info < (2, 6):
        pytest.skip("Test valid for Python 2.6+")
    inf
