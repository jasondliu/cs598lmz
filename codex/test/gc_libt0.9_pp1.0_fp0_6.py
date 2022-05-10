import gc, weakref
import os, sys
from time import time

#~ import numpy
#~ import numpy.distutils.misc_util
#~ numpy_include_dir = numpy.distutils.misc_util.get_numpy_include_dirs()

DOWNLOAD_CMD = 'wget %s -O %s'

SPC_LINK = 'http://mmc.geofisica.unam.mx/~ruben/palm/tests/small-cube.cubes'
SPC_FILE = 'small-cube.cube'

SPC512_LINK = 'http://mmc.geofisica.unam.mx/~ruben/palm/tests/small-cube512.cubes'
SPC512_FILE = 'small-cube512.cube'

RMRC_LINK = 'http://www.mmc.geofisica.unam.mx/~ruben/palm/tests/Ruben.rmrc.cubes'
RMRC_FILE = 'Ruben.rmrc.cube'

