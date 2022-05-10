import types
types.MethodType(sorted, [])

###############################################################################
#
#  ID:          $Id$
#  Date:        $Date$
#  Revision:    $Revision$
#  Source:      $Source$
#
#  Created by:  James A. Mazer (james.mazer@yale.edu)
#  Created on:  11/9/2005
#
#  Description: 
#
#  Notes:
#
###############################################################################

import sys, os, time, random, math
from popen2 import popen2
from numpy import *
from numpy.random import *
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import scipy
from scipy import interpolate
import scipy.signal
import cPickle as pickle
import types

from stimgen import *
from stimgen import stimgen
from stimgen import stimset
