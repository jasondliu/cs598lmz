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


class Model(Layer):
    """A `Model` is a graph of layers. The most common case is a
    linear stack of layers, mapping a single input to a single output.

    # Arguments
        inputs: a list of input tensors (at least one).
        outputs: a list of output tensors (at least one).
        name: an optional name string for the model.

    # Example

    ```python
        # this is a logistic regression in Keras
        x = Input
