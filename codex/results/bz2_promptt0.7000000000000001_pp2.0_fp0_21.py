import bz2
# Test BZ2Decompressor
def test_BZ2Decompressor():
    """
    >>> d = bz2.BZ2Decompressor()
    >>> for chunk in [
    ...   b"BZh91AY&SY",
    ...   b"AoEU-",
    ...   b"w"
    ... ]:
    ...   result = d.decompress(chunk)
    ...   print(result)
    hello world
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    """

# Test BZ2Decompressor.decompress
def test_BZ2Decompressor_decompress():
    """
    >>> d = bz2.BZ2Decompressor()
    >>> d.decompress(b"BZh91AY&SY")
    b'hello'
    >>> d.decompress(b"AoEU-")
    b' '
    >>> d.decompress(b"w")
    b'world\\n'
    >>> d.decompress(b"BZh91
