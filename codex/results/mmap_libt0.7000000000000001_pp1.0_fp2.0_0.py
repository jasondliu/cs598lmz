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
gflags.DEFINE_integer('width', 0, 'Width of the image')
gflags.DEFINE_integer('height', 0, 'Height of the image')
gflags.DEFINE_integer('channel', 3, 'Channel of the image')

def _map_file(input_file):
    size = os.path.getsize(input_file)
    fd = open(input_file)
    buf = mmap.mmap(fd.fileno(), size, mmap.MAP_SHARED, mmap.PROT_READ
