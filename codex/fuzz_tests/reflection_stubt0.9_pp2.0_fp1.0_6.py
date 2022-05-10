fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

from mpmath.libmp.fpstr import *

from tau import gammainc
from tau import unitstep

from mpmath.libmp.backend import xrange

from mpmath.libmp.cnfrac1 import cnfrac
from .mpmath.libmp.bnfrac1 import bnfrac
from .mpmath.libmp.cnfrac1 import cnfrac1
from .mpmath.libmp.bnfrac1 import bnfrac1

from .mpmath.libmp.libhyper import *

from mpmath.libmp.mpfi import *
from mpmath.libmp.libintmath import *

from .mpmath.libmp.libmpc import *
from .mpmath.libmp.libmpf import *
from .mpmath.libmp.libmpf import _mpf_rand_helper

from mpmath.libmp.libmpfr import *
from mpmath.libmp.numlib import *
from mpmath.libmp.mp_primes import *
from mpmath
