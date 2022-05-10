import ctypes
ctypes.cast(0, ctypes.py_object).value
 
def is_tuple(x):
    T = type(x)
    return T is tuple or T is list

def is_tuple_of(x, argtypes):
    return is_tuple(x) and len(argtypes) == len(x)

def apply_generic(method, args):
    # Readability, pylint: disable=line-too-long
    types = (ctypes.py_object,) + tuple(map(type, args))
    for T in npy_types:
        if T is not ctypes.py_object and is_tuple_of(args, T):
            return getattr(method, '{}'.format(T.__name__))(*args)
    raise TypeError('No version of %s supports types %s' % (method, types))

def get_node_by_id(idx): return get_node(nx.to_numpy_repr(idx))

def reduce_add(nodes): return get_node_by_id(
