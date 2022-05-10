import types
types.ModuleType = ModuleType
import torch._C as _C

def _array_size(shape, dtype=None):
    if isinstance(shape, tuple) and len(shape) > 0 and hasattr(shape[0], '__index__'):
        # support non-tuple sequences, e.g., generator expressions
        shape = tuple(size.__index__() for size in shape)
    if dtype is not None:
        dtype = _C._int_to_void_p(dtype.id)
    return torch.LongTensor(list(shape)).storage().size() * 4, dtype

