import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def serialize(data, idx, context):
    # Context may be None, or an index into the context tuple.

    #### Dictionary
    if isinstance(data, dict):
        yield (('dict', len(data)), idx)
        for key in sorted(data.keys()):
            for x in serialize(key, None, context):
                yield x
            for x in serialize(data[key], None, context):
                yield x

    #### List
    elif isinstance(data, list):
        yield (('list', len(data)), idx)
        for x in data:
            for y in serialize(x, None, context):
                yield y

    #### Tuple
    elif isinstance(data, tuple):

        #### Named tuple
        if hasattr(data, '_fields'):
            yield (('tuple', data.__class__.__name__, len(data)), idx)
            context = context + (data,)
            idx = None
            for field in data._fields:
                for x in serialize
