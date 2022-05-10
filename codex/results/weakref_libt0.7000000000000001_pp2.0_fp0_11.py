import weakref

import numpy as np
from brian2 import Equations, stdunits, check_units, DimensionMismatchError, \
    get_dimensions, second, Unit, get_unit_fast, all_units, Quantity, \
    IncompatibleDimensionsError, Dimension

from brian2.core.namespace import get_local_namespace
from brian2.core.functions import Function, DEFAULT_FUNCTIONS
from brian2.core.variables import *
from brian2.core.preferences import brian_prefs
from brian2.equations.equations import DIFFERENTIAL_EQUATION, SUBEXPRESSION, \
    PARAMETER, CONSTANT, BOOLEAN, INTEGER, FLOAT, STRING, \
    DIFFERENTIAL_EQUATION_REGEX, ABSTRACT_TYPE, AbstractEquations
from brian2.equations.codestrings import (DEFAULT_FUNCTIONS_CODE,
                                          DEFAULT_FUNCTION_IMPLEMENTATIONS_CODE)
from b
