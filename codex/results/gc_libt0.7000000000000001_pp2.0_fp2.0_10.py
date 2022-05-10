import gc, weakref

from . import _check_args

def csr_matrix(arg1, shape=None, dtype=None, copy=False):
    """
    This function is used to construct a sparse matrix from
    dense matrix or from any object exposing the array interface.

    In addition to the form of dense matrix input described below,
    this function can construct a matrix from
    any object that gives access to arrays.  This includes
    matrices, sparse matrices, and ``scipy.sparse`` representations of
    graphs.

    Parameters
    ----------
    arg1 : array_like or sparse matrix
        2-D array to be compressed. If `shape` is not given, `arg1`
        must be a square matrix.

    shape : tuple, optional
        Shape of the result. Only required if `arg1` is not a square
        matrix.

    dtype : dtype, optional
        The value type of the matrix. If not specified, the value
        type is determined from the type of values in `arg1`.
        Note that `float` and `complex` are not allowed for dtype
