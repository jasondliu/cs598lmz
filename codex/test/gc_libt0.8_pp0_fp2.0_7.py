import gc, weakref
import numpy as np

from contextlib import closing

import logging
logger = logging.getLogger(__name__)

from ctypes import c_size_t

