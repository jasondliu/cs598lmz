import _struct

import numpy as np

import pytest

import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.nn.modules.utils import _pair
from torch.autograd import gradcheck

from common_utils import TestCase, run_tests, IS_WINDOWS
from common_utils import skipIfRocm, skipIfNoLapack, suppress_warnings, skipCUDANonDefaultStream
from common_utils import skipCUDAIfRocm, skipCUDAIfNoMagma, skipCUDAIfNoLapack, skipCUDAIfNotRocm

from torch.testing._internal.common_utils import random_fullrank_matrix_distinct_singular_value

if torch.cuda.is_available():
    import torch.cuda.comm as comm
    from torch.cuda.comm import broadcast
    from torch.cuda.comm import reduce_add
    from torch.cuda.comm import reduce_add_coalesced
    from torch.cuda.comm import reduce_mult
