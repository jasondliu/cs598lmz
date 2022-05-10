import gc, weakref
import numpy as np

from numpy.lib.stride_tricks import as_strided

from . import window


class Buffer(object):
    """
    A class to represent memory buffers.

    Buffer instances are windowable, so to create a rolling buffer,
    simply use the rolling() method.

    Buffer instances are hashable.

    Buffer instances are automatically garbage collected, as long
    as the underlying memory has not been deallocated.

    Buffer instances can be sliced using numpy array indexing syntax.
    This is lazy, so memory is not copied, and the underlying memory
    is not deallocated until the last reference to the slice is gone.

    Buffer instances can be concatenated using numpy array indexing
    syntax.  This is lazy, so memory is not copied, and the underlying
    memory is not deallocated until the last reference to the
    concatenated buffer is gone.

    Buffer instances can be compared by value to other Buffer instances,
    or to tuples, lists, or other sequences.  If a sequence is used,
    it is compared to the underlying memory.

   
