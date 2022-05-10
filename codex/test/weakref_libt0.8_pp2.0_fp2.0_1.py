import weakref
import copy

import numpy as np

from rlpyt.utils.buffer import buffer_to, buffer_method
from rlpyt.utils.quick_args import save__init__args
from rlpyt.utils.logging import logger
from rlpyt.utils.collections import AttrDict
from rlpyt.utils.misc import copy_attrs, maybe_iter
from rlpyt.utils.tensor import valid_mean
from rlpyt.replays.non_sequence.uniform import UniformReplayBuffer

# TRANSITION_BUFFER_SIZE = 512  # for use with a batch size of 32
# TRANSITION_BUFFER_SIZE = 1024  # for use with a batch size of 64
TRANSITION_BUFFER_SIZE = 256  # for use with a batch size of 64


