import weakref
import functools
import itertools
from collections import deque

import gc

import torch
import torch.distributed as dist
from torch._utils import _get_device_index
from torch._six import with_metaclass

from . import ProcessGroupGloo as _ProcessGroupGloo
from . import ProcessGroupNCCL as _ProcessGroupNCCL
from . import ProcessGroupMPI as _ProcessGroupMPI
from . import ProcessGroupStore as _ProcessGroupStore
from . import ProcessGroupAgent as _ProcessGroupAgent


# TODO(#38095): Replace with torch.distributed.autograd once it's finalized.
def _dist_broadcast_coalesced(tensors, buffer_size):
    # buffer size in bytes
    buffer_size = int(buffer_size)

    world_size = dist.get_world_size()

    buffers = []
    if not dist.get_rank() == 0:
        tensors = [torch.empty_like(t) for t in tensors]
