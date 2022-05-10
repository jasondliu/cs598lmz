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
