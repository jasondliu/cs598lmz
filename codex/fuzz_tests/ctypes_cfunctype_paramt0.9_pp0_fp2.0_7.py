import ctypes
FUNTYPE = ctypes.CFUNCTYPE( C.c_long, C.c_long )

def case( from_, to_, fun_ ):
    gulp_inpu_state.add( from_, fun_ )
    return GULP_CASE(from_, to_)

from liblibra_core import *
from libra_py import *
from libra_py.workflows.nbra.timepropagation import propagators
from libra_py.workflows.nbra.timepropagation.propagator_parameters import *

from libra_py.workflows.nbra.timepropagation import propagators
from libra_py.workflows.nbra.timepropagation.propagator_parameters import global_parameters

from pyre.units.time import fs
from pyre.units.length import bohr as b, angstrom as ang
from pyre.units.energy import kcal
from pyre.units.mass import amu
from pyre.units.frequency import inv_cm
from pyre.units.pressure import atm
from pyre.units.
