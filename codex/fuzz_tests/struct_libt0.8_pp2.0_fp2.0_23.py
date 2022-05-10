import _struct
from abc import ABC, abstractmethod
from collections import defaultdict, OrderedDict
from copy import copy
from dataclasses import dataclass
from enum import Enum
from functools import partial
from io import BytesIO
from math import floor, log, sqrt

from sortedcontainers import SortedDict
from typing import Dict, Any, List, Union, Tuple, Set, Callable, Optional, TypeVar

from . import mkldnn_types, tensor
from mxnet.gluon import HybridBlock
from mxnet.symbol import Symbol, SymbolHandle
from mxnet.ndarray import NDArray, zeros
from mxnet.base import _LIB, check_call
from mxnet.util import use_np_shape, is_np_shape, is_np_array, use_np_array


class _ExecutorGroup(ABC):
    """An group of executors that can run/eval concurrently."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
