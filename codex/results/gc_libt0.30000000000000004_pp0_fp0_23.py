import gc, weakref

import numpy as np

from . import _pywrapfem
from . import _pywrapfem_utils
from . import _pywrapfem_geometry
from . import _pywrapfem_mesh
from . import _pywrapfem_postprocessing
from . import _pywrapfem_solver
from . import _pywrapfem_solver_utils
from . import _pywrapfem_solver_utils_assemble
from . import _pywrapfem_solver_utils_boundary_conditions
from . import _pywrapfem_solver_utils_materials
from . import _pywrapfem_solver_utils_solution
from . import _pywrapfem_solver_utils_solution_fields
from . import _pywrapfem_solver_utils_solution_fields_operators
from . import _pywrapfem_solver_utils_solution_fields_operators_integration
from . import _pywrapfem_solver_utils_solution_fields_operators_integration_rules

