import bz2
# Test BZ2Decompressor
if bz2.decompress(test_compr) == test_orig:
    print('Same data')

decompressor = bz2.BZ2Decompressor()
# Use multiple decmpress calls to get all data
decompressed_data = decompressor.decompress(test_compr)
decompressed_data += decompressor.flush()
if decompressed_data == test_orig:
    print('Same data')

###############################################################################
# Find the python executable
# -----------------------------------------------------------------------------
import sys
sys.executable
# Change running executable
# execfile(sys.executable)

###############################################################################
# Format strings
# -----------------------------------------------------------------------------
# f-Strings are supported as of Python 3.6
# format strings are more powerful
# f-strings:
a = 1234
formula = '{0:d}'.format(a)
formula = '{0:5d}'.format(a)
formula = '{0:05d}'.format(a)
formula = '{0:o}'.format(a)
form
