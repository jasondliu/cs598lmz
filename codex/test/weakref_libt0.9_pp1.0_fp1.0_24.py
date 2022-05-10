import weakref
import gc

import pandas as pd
from IPython.config.loader import JSONConfigFile
from IPython.parallel import requires_multiprocessing, ipclient
from IPython.utils.traitlets import Instance
from natsort import natsorted
from suqc.utils import guess_module_file, check_valid_module
from suqc.utils.logger import get_logger
from .feature_extractor import FeatureExtractor
from .stardis_caller import stardis, stardis_pipe, stardis_pipe_runner
from .validators import ValidWaveletFilter
from imageio import imread

if not requires_multiprocessing:
    raise NotImplementedError("Requires IPython >= 1.1")
logger = get_logger("suqc.ipython.parallel")


