import gc, weakref

import numpy as np
import numpy.linalg as la

__all__ = ['Basis', 'Array', 'add_index', 'NullSpace', 'Interior',
           'Exterior', 'DefaultIndex', 'DirectIndexSet', 'resolve_indices']

class IndexSet(object):
    """A set of indices.

    Index sets have an identity.  Index sets with the same identity are
    considered to be equivalent.  This allows them to be distinguished
    from other index sets but still be used as the same index set.

    The default implementation of the identity is the memory address of the
    set, so by default index sets are distinguished by their memory address.

    """

