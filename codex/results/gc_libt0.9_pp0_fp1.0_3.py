import gc, weakref
import math, pickle

import vxi11

from . import constants
from .hookable import Hookable
from .device_exceptions import DeviceError, DeviceException
from .errors import errors
from .constants import TriggerSlope, TriggerCoupling, TriggerSource, MeasFunction, Parameter, ReferenceSource, ReferenceTie, Coupling, Range, Autozero, PowerLineFrequency, OutputFunction, OutputWaveform, trigger_slope_to_thesaurus, trigger_coupling_to_thesaurus, trigger_source_to_thesaurus, meas_function_to_thesaurus, parameter_to_thesaurus, reference_source_to_thesaurus, reference_tie_to_thesaurus, coupling_to_thesaurus, range_to_thesaurus, autozero_to_thesaurus, powerline_frequency_to_thesaurus, output_function_to_thesaurus, output_waveform_to_thesaurus
from .instrospection import InstrospectionYear


g_logger = logging.getLogger('rigol.device')


