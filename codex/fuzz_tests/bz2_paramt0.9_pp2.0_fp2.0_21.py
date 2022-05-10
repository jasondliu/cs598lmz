from bz2 import BZ2Decompressor
BZ2Decompressor()
# is equivalent to:
decompress = BZ2Decompressor().decompress
decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'
          b'\x9e\x46\x33\x88\x6d\x19\x00\x21\x08\x04')
b'BZh91AY&SY\x9eF3\x88m\x19\x00!\x08\x04'
</code>

