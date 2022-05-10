import weakref

import numpy as np

from brian2.core.base import BrianObject
from brian2.core.namespace import get_local_namespace
from brian2.core.preferences import prefs, brian_prefs
from brian2.core.variables import Constant, Subexpression, AuxiliaryVariable, Variables
from brian2.groups.group import CodeRunner, Group, get_dtype
from brian2.units.fundamentalunits import check_units, get_unit
from brian2.units.allunits import second, Hz, mV
from brian2.utils.logger import get_logger
from brian2.utils.stringtools import get_identifiers, word_substitute

__all__ = ['BrianObject2', 'NetworkOperation', 'NetworkOperationGroup',
           'NetworkOperationScheduler']

logger = get_logger(__name__)


