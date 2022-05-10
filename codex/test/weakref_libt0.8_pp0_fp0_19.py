import weakref

import numpy as np
import pymatgen as mg
from pymatgen.analysis.structure_matcher import StructureMatcher
import xarray as xr
from pymatgen.io.vasp import Vasprun
from pymatgen.io.vasp.inputs import Poscar
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from sumo.symmetry.standardized_sites import standardize_sites

from sumo.io.smartio import SmartIo
from sumo.io.vaspio_direct import (
    PoscarIo,
    KpointsIo,
    IncarIo,
    PotcarIo,
)
from sumo.symmetry.equiv_sites import EquivSiteGrouper
from sumo.util.tolerance import get_tol, get_dist_tol

