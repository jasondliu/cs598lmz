import gc, weakref
import numpy as np
from numpy import pi
from numpy.linalg import norm

from pyNastran.op2.tables.oqg_constraintForces.oqg_spcForces import SPCForcesObject
from pyNastran.op2.tables.oqg_constraintForces.oqg_mpcForces import MPCForcesObject
from pyNastran.bdf.bdf import BDF
from pyNastran.op2.op2 import OP2
from pyNastran.f06.f06_formatting import write_floats_13e, _eigenvalue_header
from pyNastran.op2.tables.geom.geom_common import GeomCommon
from pyNastran.op2.tables.geom.geom1 import GEOM1
from pyNastran.op2.tables.geom.geom2 import GEOM2
from pyNastran.op2.tables.geom.geom3 import GEOM3
from pyNast
