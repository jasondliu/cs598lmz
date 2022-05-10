from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(f)
</code>
And as noted by @GordThompson in the comments, this trick only works from Python 3.3 onward.

