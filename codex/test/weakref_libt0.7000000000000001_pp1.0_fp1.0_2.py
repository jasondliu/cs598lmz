import weakref
from os import path
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional, Tuple, Union, cast

import numpy as np
from monty.json import MSONable
from pydantic import Field, BaseModel, validator
from pymatgen import MPRester, Structure
from pymatgen.core.composition import Composition
from pymatgen.core.periodic_table import Element, Specie

from mpcat.utils.decomposition import get_decomposition_stoichs
from mpcat.utils.decomposition import get_decomposition_stoichs_full_elemental_comp
from mpcat.utils.decomposition import get_decomposition_stoichs_full_structure
from mpcat.utils.decomposition import validate_decomposition_stoichs
from mpcat.utils.decomposition import validate_decomposition_stoichs_full_structure
from mpcat.utils.decomposition import validate_decomposition_stoichs_full_elemental
