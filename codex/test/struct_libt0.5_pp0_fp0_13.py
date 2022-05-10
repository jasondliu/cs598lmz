import _struct

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

def _get_type_size(dtype, field_name=None):
    """
    Return the size of a dtype.

    Parameters
    ----------
    dtype : dtype
        dtype to get size of.

    Returns
    -------
    size : int
        Size of dtype in bytes.
    """
    if isinstance(dtype, np.dtype):
        if field_name is None:
            return dtype.itemsize
