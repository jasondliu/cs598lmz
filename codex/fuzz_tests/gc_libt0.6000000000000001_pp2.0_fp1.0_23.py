import gc, weakref
from collections import defaultdict
import logging

import numpy as np

from nengo.builder.builder import Builder
from nengo.builder.signal import Signal
from nengo.builder.operator import Operator, Copy, Reset
from nengo.connection import LearningRule
from nengo.ensemble.ensemble import Ensemble
from nengo.ensemble.neurons import LIF, LIFRate, Direct
from nengo.exceptions import BuildError, ValidationError
from nengo.node import Node
from nengo.neurons import Direct
from nengo.synapses import Lowpass, SynapseParam
from nengo.utils.compat import is_iterable, range, iteritems, itervalues

logger = logging.getLogger(__name__)


class SignalDict(dict):
    """Dict that tracks whether its values are fresh or not.

    This is used for storing signals.

    Parameters
    ----------
    shape : tuple
        Shape of the signals that will be stored.
    dtype : dtype, optional
