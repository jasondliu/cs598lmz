import gc, weakref

from numpy import *
from numpy.linalg import *
from numpy.random import *
from numpy.testing import *

# do not import scipy.linalg in namespace
from scipy.linalg.misc import *
from scipy.linalg import norm, det
from scipy.linalg import expm as expm1

from scipy.linalg import inv as inv1
from scipy.linalg import pinv as pinv1
from scipy.linalg import pinv2 as pinv2_alias
from scipy.linalg import solve as solve1
from scipy.linalg import lstsq as lstsq1
from scipy.linalg.decomp_lu import *
from scipy.linalg import expm

