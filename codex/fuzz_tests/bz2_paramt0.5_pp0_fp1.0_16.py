from bz2 import BZ2Decompressor
BZ2Decompressor()

import os
import shutil
import tempfile
import warnings
import zipfile

import numpy as np

from sklearn.externals.joblib import Memory, logger
from sklearn.externals.joblib.parallel import Parallel, delayed
from sklearn.externals.joblib.format_stack import format_exc
from sklearn.utils import deprecated

# When working on the code of joblib, it is useful to reload the module
# automatically at each call for rapid testing
AUTORELOAD_JOBLIB = int(os.environ.get('JOBLIB_MULTIPROCESSING', 0))

# The directory in which we will store the temporary files when
# Backend='tempfolder'
_TEMP_FOLDER = tempfile.mkdtemp(prefix='joblib_memmapping_folder_',
                                dir=os.environ.get('JOBLIB_TEMP_FOLDER', None))

# The size of the chunks that are read and written by the memmaping
# backend.
MEMMAPING_HANDLER_READ
