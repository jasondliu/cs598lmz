from lzma import LZMADecompressor
LZMADecompressor()
# if LZMADecompressor() throws an exception, then you need to install pyliblzma.
# see note above.

import numpy
numpy.__version__
# try again if you get "TypeError: ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''"


