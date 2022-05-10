import weakref

import numpy as np

from . import _utils
from . import _backend
from . import _backend_utils


class _BaseLayer:
    """
    Base class for all layers.
    """

    def __init__(self, name=None, dtype=None, **kwargs):
        self._name = name
        self._dtype = dtype
        self._params = []
        self._regularizers = []
        self._constraints = []
        self._trainable_weights = []
        self._non_trainable_weights = []
        self._updates = []
        self._losses = []
        self._inbound_nodes = []
        self._outbound_nodes = []
        self._input_mask = None
        self._output_mask = None
        self._input_shape = None
        self._output_shape = None
        self._input_dtype = None
        self._output_dtype = None
        self._activity_regularizer = None
        self._trainable = True
        self._sparse_input
