import types
types.SimpleNamespace.__repr__ = lambda self: "%s(%s)" % (self.__class__.__name__, ", ".join("%s=%s" % item for item in vars(self).items()))

from .types import (
    Model,
    Batch,
    Generic,
    GenericModel,
    GenericBatch,
    GenericEncoder,
    GenericDecoder,
    GenericModelMNIST,
    GenericEncoderMNIST,
    GenericDecoderMNIST,
    GenericBatchMNIST,
)
from .utils import (
    create_model,
    create_batch,
    create_encoder,
    create_decoder,
    create_criterion,
    create_optimizer,
    create_scheduler,
    get_model_parameters,
    get_model_gradients,
    get_model_buffers,
    get_batch_data,
    get_batch_target,
    get_batch_loss,
    get_optimizer_param_groups,
    get_optimizer_parameters,
