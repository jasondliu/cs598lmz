import bz2
# Test BZ2Decompressor
# This has been tested on Python 2.7.
#  
# NOTE: The result of decompression is not identical to the result of the 
# original decompressor that is used in the Python 2.7 bz2 module. This 
# might be due to randomness in the compression algorithm that is not 
# deterministic. The original decompressor is probably doing something 
# to the random number generator to make the result deterministic. 
# The output of the decompressor is checked for integrity using the 
# sha256 checksum and the result of the original decompressor.
#
# This decompressor can not handle the decompression of multiple bz2 compressed
# streams in one go. 
#
# The decompressor is also tested against a test suite that can be found on 
# https://sourceware.org/ml/bzip2/2007-q1/msg00004.html .
#
# The decompressor is also tested against a test suite found on 
# https://github.com/indygreg/python-bzip2/blob/master/src/bz2file.py
#

#
