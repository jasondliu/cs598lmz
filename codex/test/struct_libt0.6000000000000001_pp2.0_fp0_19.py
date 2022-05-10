import _struct

# #############################################################################
# Constants
# #############################################################################

_NONE_SENTINEL = object()

# #############################################################################
# Helpers
# #############################################################################

def _get_dtype(obj):
    """Get the dtype of an object.
    """
    return getattr(obj, 'dtype', None)

def _get_shape(obj):
    """Get the shape of an object.
    """
    try:
        return obj.shape
    except AttributeError:
        return ()

def _get_strides(obj):
    """Get the strides of an object.
    """
    try:
        return obj.strides
    except AttributeError:
        return ()

def _get_writeable(obj):
    """Get the writeable flag of an object.
    """
    try:
        return obj.writeable
    except AttributeError:
        return False

def _get_data(obj):
    """Get the data buffer of an object.
    """
