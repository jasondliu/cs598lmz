import lzma
# Test LZMADecompressor

# Stolen from https://stackoverflow.com/questions/14230138/lzma-decompression-in-python

# Note: the lzma module was added in Python 3.3

# This code is optimized for speed, not readability.
# It is ~15x faster than the corresponding code in Python 2.7.6

# It doesn't support concatenated streams.

# The code is based on the C code by Igor Pavlov in lzma/C/LzmaDec.c
# which is part of the LZMA SDK (http://www.7-zip.org/sdk.html)

# The LZMA SDK is licensed under the Common Public License v1.0
# (http://opensource.org/licenses/cpl1.0.php)

# The LZMA SDK is written and placed in the public domain by Igor Pavlov.

# The LZMA SDK (C) 1999-2013 Igor Pavlov

# The LZMA SDK is written and placed in the public domain by Igor Pavlov.
# The library is free for
