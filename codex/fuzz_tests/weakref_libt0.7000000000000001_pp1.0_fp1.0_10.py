import weakref
from collections import OrderedDict

from rlpyt.utils.logging import logger
from rlpyt.utils.buffer import buffer_to, buffer_func
from rlpyt.utils.collections import AttrDict, NamedTupleSchedule
from rlpyt.utils.tensor import infer_leading_dims, restore_leading_dims, print_size_of
from rlpyt.models.mlp import MlpModel
from rlpyt.models.conv2d import Conv2dModel
from rlpyt.models.utils import update_state_dict
from rlpyt.utils.quick_args import save__init__args
from rlpyt.utils.seed import set_seed, make_seed
from rlpyt.utils.dtypes import global_np_dtype
from rlpyt.models.utils import count_parameters as _count_parameters
from rlpyt.models.rl.base import BaseModel
import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_
