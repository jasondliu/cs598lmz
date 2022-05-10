import ctypes
ctypes.cdll.LoadLibrary('/net/hciserver03/storage/pboes/projects/TDF_MODELS/hcpe_pipeline/tools/freesurfer/lib/libmri.so')
ctypes.cdll.LoadLibrary('/net/hciserver03/storage/pboes/projects/TDF_MODELS/hcpe_pipeline/tools/freesurfer/lib/libgcutil.so')
ctypes.cdll.LoadLibrary('/net/hciserver03/storage/pboes/projects/TDF_MODELS/hcpe_pipeline/tools/freesurfer/lib/libutils.so')

import nibabel as nib
import numpy as np
from sys import argv
import os.path as path
import sys
import os
import time
import glob
import numpy
import numpy.linalg as npl
from numpy import *

#def solve_system(lhs, rhs):
#    a = dot(lhs.T, lhs)
#   
