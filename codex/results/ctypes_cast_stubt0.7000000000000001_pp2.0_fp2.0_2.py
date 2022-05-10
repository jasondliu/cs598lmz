import ctypes
ctypes.cast(0, ctypes.py_object).value = None

from collections import OrderedDict
import numpy as np
import os

import qcodes as qc
from qcodes.utils.helpers import strip_attrs
from qcodes.tests.instrument_mocks import DummyInstrument
from qcodes.instrument.parameter import ArrayParameter, Parameter
import qcodes.instrument.base
from qcodes.instrument.base import InstrumentBase
from qcodes.instrument.group_parameter import GroupParameter
from qcodes.instrument.base import Instrument
from qcodes.instrument.base import InstrumentChannel
from qcodes.instrument.parameter import ManualParameter
from qcodes.instrument.parameter import Parameter
from qcodes.instrument.parameter import MultiParameter
from qcodes.instrument.parameter import ArrayParameter
from qcodes.instrument.parameter import DelegateParameter
from qcodes.instrument.parameter import _Parameter
from qcodes.instrument.parameter import _ParameterWithSetpoints
from qcodes.utils.validators import Numbers, Ints, En
