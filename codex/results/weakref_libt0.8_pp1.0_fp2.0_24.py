import weakref

from hiclib.fragmentHiC import HiCdataset
from mirnylib.systemutils import setExceptionHook
import numpy as np

from hiclib.hicShared import mapDistToTADs
from mirnylib.h5dict import h5dict
import pylab
import sys
from optparse import OptionParser

from mirnylib import genome
from mirnylib import plotting
from mirnylib.numutils import completeIC
from mirnylib.systemutils import setExceptionHook
from hiclib import binnedData
from mirnylib.genome import Genome
from mirnylib.systemutils import setExceptionHook
from hiclib import fragmentHiC
from hiclib.fragmentHiC import HiCdataset
from mirnylib import numutils
import mirnylib.numutils
import os
from optparse import OptionParser
import os
import h5py
import numpy
import numpy.lib.recfunctions
import matplotlib.pyplot as plt
import sys
import
