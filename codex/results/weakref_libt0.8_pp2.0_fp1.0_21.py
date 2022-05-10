import weakref

import numpy as np

from pymatgen.core.structure import Structure
from pymatgen.io.vasp.inputs import Kpoints
from pymatgen.io.vasp.sets import MPRelaxSet
from pymatgen.io.vasp.sets import VaspInputSet
from pymatgen.io.vasp.sets import UnconvergedVaspError
from pymatgen.io.vasp.sets import Incar
from pymatgen.io.vasp.sets import Potcar
from pymatgen.io.vasp.outputs import Outcar, Vasprun
from pymatgen.io.vasp.outputs import UnconvergedVaspError as OutcarUnconverged
from pymatgen.io.vasp.outputs import BSVasprun
from pymatgen.io.vasp.outputs import ZPOSCAR
import pymatgen.io.vasp.inputs as vasp_input
import pymatgen.io.vasp.outputs as vasp_out

