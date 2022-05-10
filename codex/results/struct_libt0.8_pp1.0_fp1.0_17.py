import _struct

class DaskObject(object):
    def __array__(self):
        from . import array as da
        return da.from_array(numpy.asarray(self))


class Array(DaskObject):
    """ Represents a collection of values

    This is a core data structure of dask.  A ``dask.Array`` consists of a number
    of smaller ``numpy.ndarray`` objects on a grid.  We store a small chunk
    of the entire array in each location.

    You typically create a ``dask.Array`` by calling a function on a
    ``dask.Array`` like ``x.map_blocks(myfunc)``.

    You can also explicitly create one by passing in a tuple of blocks, a tuple
    of shapes, a tuple of blockdims, and a single chunksize

    Parameters
    ----------

    name : str
        The key prefix that specifies which keys in the dask graph correspond
        to this array
    chunks : tuple
        The block shape along each dimension
    dtype : str or dtype
        Data type of the array
    graph
