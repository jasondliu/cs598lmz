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
