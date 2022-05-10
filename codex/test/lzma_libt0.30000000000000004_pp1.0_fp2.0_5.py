import lzma
lzma.LZMAFile

# The following is a hack to fix the issue with the lzma module
# not being able to find the liblzma.so.5 library.
# See https://bugs.python.org/issue24688 for details.
import ctypes
ctypes.cdll.LoadLibrary("liblzma.so.5")

import numpy as np
import pandas as pd
