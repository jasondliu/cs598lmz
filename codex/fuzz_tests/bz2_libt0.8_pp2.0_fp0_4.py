import bz2
bz2.BZ2Compressor()

# Test fix for bug #29570.  Test needs to be run 
# with -Wdefault and a debug build.  Let the warning go.
# (This test is copied from test_lzma, with a few modifications.)
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', '.*buffer size mismatch.*',
                            RuntimeWarning)
    import lzma
    lzma.LZMACompressor()

# Test fix for bug #29924.  Test needs to be run under a
# platform that supports the posix flags O_NOATIME and O_NOFOLLOW.
# These are not currently implemented on Windows.
import os
if hasattr(os, 'O_NOATIME'):
    file = os.open(__file__, os.O_RDONLY | os.O_NOATIME)
    if hasattr(os, 'O_NOFOLLOW'):
        file = os.open(__file__, os.O_RDONLY | os.O_NOATIME | os
