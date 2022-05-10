import weakref

from collections import namedtuple
from functools import wraps
from numbers import Real
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

from numpy import array, asarray, concatenate, empty, ndarray, ones, vstack, zeros
from scipy import sparse

from openmdao.api import ExplicitComponent
from openmdao.core.component import Component
from openmdao.core.driver import Driver, DriverComp
from openmdao.core.explicitcomponent import ExplicitComponent as ExplicitComponentBase
from openmdao.core.group import Group
from openmdao.core.indepvarcomp import IndepVarComp
from openmdao.core.system import System
from openmdao.core.vec_wrapper import VecWrapper
from openmdao.devtools.problem_viewer.problem_viewer import _get_viewer_data
from openmdao.jacobians.assembled_jacobian import AssembledJacobian
from openmdao.matrices.coo_matrix import COOMatrix
from openmd
