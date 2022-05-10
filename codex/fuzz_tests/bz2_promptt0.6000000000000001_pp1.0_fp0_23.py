import bz2
# Test BZ2Decompressor

"""
>>> d = BZ2Decompressor()
>>> d.decompress(b"BZh91AY&SY")
b"hello"
>>> d.decompress(b"BZh91AY&SY")
b""
>>> d.decompress(b"BZh91AY&SY")
Traceback (most recent call last):
...
EOFError: Compressed file ended before the end-of-stream marker was reached
>>> d.decompress(b"BZh91AY&SY")
Traceback (most recent call last):
...
EOFError: Compressed file ended before the end-of-stream marker was reached
>>> d.decompress(b"BZh91AY&SY")
Traceback (most recent call last):
...
EOFError: Compressed file ended before the end-of-stream marker was reached
>>> d.decompress(b"BZh91AY&SY")
Traceback (most recent call last):
...
EOFError: Compressed file ended before the end-of-stream marker was reached
>>>
