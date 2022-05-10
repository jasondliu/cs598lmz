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

    __metaclass__ = abc.ABCMeta

    def __eq__(self, other):
        return self is other

    def __ne__(self, other):
        return self is not other

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return "%s(%r)" % (type(self).__name__, self.
