import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

import os
import sys
import time
import traceback
import types
import unittest

import numpy as np

import torch
import torch.cuda
import torch.cuda.comm as comm
import torch.cuda.nccl
import torch.distributed as dist
import torch.multiprocessing as mp
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data
import torch.utils.data.distributed

from common import (TEST_WITH_TSAN, skip_if_not_multigpu, skip_if_rocm,
                    skip_if_small_worldsize, skip_if_no_cuda_distributed,
                    skip_if_no_nccl, skip_if_no_cudnn,
                    skip_if_lt_x_gpu, skip_if_not_multigpu,
                    skip_if_not_built_with_cuda,
                    get_gpu
