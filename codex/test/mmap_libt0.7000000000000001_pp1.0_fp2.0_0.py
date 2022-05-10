import mmap
import numpy as np
import shutil
import struct
import sys
import time

import gflags

from scipy import misc
from skimage import io

FLAGS = gflags.FLAGS

gflags.DEFINE_string('input', '', 'Name of input file')
gflags.DEFINE_string('output', '', 'Name of output file')
gflags.DEFINE_string('format', '', 'Format of the image')
gflags.DEFINE_integer('stride', 512, 'Stride of the image')
