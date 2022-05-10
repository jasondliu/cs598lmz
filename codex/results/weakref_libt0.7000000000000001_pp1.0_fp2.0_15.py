import weakref

import numpy as np
import pymongo
import pytest

import pymatgen
from pymatgen.core.periodic_table import Element
from pymatgen.core.structure import Structure
from pymatgen.core.composition import Composition
from pymatgen.entries.computed_entries import ComputedEntry, \
    ComputedStructureEntry
from pymatgen.analysis.phase_diagram import PhaseDiagram
from mpinterfaces.calibrate import ComputedEntryLazyMongoDb
from pymatgen.analysis.phase_diagram import PDPlotter
from pymatgen.core.units import all_units
from pymatgen.core.periodic_table import Element, Specie
from pymatgen import Composition, MPRester
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.entries.computed_entries import ComputedEntry, ComputedStructureEntry
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen
