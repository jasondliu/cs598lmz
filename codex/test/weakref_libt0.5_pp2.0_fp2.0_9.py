import weakref

import numpy as np

from . import backend as K
from .engine.topology import InputSpec, Layer, Merge
from .engine.topology import get_source_inputs, Node, create_layer
from .layers import Embedding, Input, Masking, Reshape, TimeDistributed
from .utils.generic_utils import unpack_singleton
from .utils.layer_utils import add_loss
from .utils.np_utils import to_categorical
from .utils.serialize import serialize, deserialize
from .utils.training_utils import standardize_input_data


