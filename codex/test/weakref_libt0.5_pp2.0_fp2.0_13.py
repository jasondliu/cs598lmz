import weakref
import warnings
from collections import defaultdict
from contextlib import contextmanager
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type, Union

import torch
from torch import Tensor

from ignite.engine import Engine, Events
from ignite.metrics import Metric
from ignite.metrics.metric import reinit__is_reduced, sync_all_reduce
from ignite.utils import to_onehot

from .metrics import (
    _check_num_classes,
    _check_predictions,
    _check_targets,
    _prepare_batch,
    _prepare_targets,
)


class _State:
    def __init__(self, num_classes: int, average: str = "binary"):
        self.num_classes = num_classes
        self.average = average
        self.reset()

    def reset(self) -> None:
        self.sum_cm = torch.zeros(self.num_classes, self.num_classes)
