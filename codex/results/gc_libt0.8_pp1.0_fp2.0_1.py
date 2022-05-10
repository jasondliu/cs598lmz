import gc, weakref
import torch.multiprocessing as mp
import torch.utils.data

from multiprocessing.pool import ThreadPool
from multiprocessing import TimeoutError
from torch.utils.data import Dataset
from torch._utils import _accumulate
from itertools import repeat

import numpy as np
import random
import cv2

__all__ = ['ParallelLoader', 'ParallelWriter']

_use_shared_memory = False
"""Whether to use shared memory in default_collate"""

random.seed(1234)


def default_collate(batch):
    r"""Puts each data field into a tensor with outer dimension batch size"""
    elem_type = type(batch[0])
    if isinstance(batch[0], torch.Tensor):
        out = None
        if _use_shared_memory:
            # If we're in a background process, concatenate directly into a
            # shared memory tensor to avoid an extra copy
            numel = sum([x.numel() for x in batch])
            storage = batch[
