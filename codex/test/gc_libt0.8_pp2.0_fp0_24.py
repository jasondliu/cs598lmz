import gc, weakref, os, sys

import numpy as np

if sys.version_info[0] == 2:
    from Queue import Empty, Queue
    range = xrange
    from itertools import izip_longest as zip_longest
else:
    from queue import Empty, Queue
    from itertools import zip_longest

__all__ = ['Array', 'TreeArray']

class Array(np.ndarray):
    """ An Array is a :class:`numpy.ndarray` that supports a form of ``del`` syntax.
    It is meant to be used at the top level of the array tree.

    Attributes
    ----------

    parents : :class:`~dolo.numeric.decision_rule.DecisionRule`
        A list of objects that should be called when `__delattr__` is called.
        This is necessary to control the order in which things are deleted.
    """
