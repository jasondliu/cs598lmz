import lzma
lzma.LZMAFile

# TODO: Remove this hack once we have a proper solution to the
#       "import lzma" problem.
lzma_is_available = True

import os
import shutil
import sys
import tempfile
import zipfile

import numpy as np

# TODO: Remove this hack once we have a proper solution to the
#       "import lzma" problem.
if lzma_is_available:
    import lzma
else:
    import backports.lzma as lzma

