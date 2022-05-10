from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(chunk).splitlines()
</code>
For toil's local docker calls, multiprocessing is used, and for more information about how toil does it, look at their source code.

