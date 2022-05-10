import gc, weakref
import random, threading

try:
    import cPickle as pickle
except ImportError:
    import pickle

from multipr.util import get_namedtuple_pickle, get_namedtuple_pickle

yappi_imported = False
try:
    import yappi
    yappi_imported = True
except ImportError:
    pass


#####################################################################
#
# Queue Extensions
#
#####################################################################

class mp_sasyncresult(multiprocessing.SAsyncResult):
    """Modified version of mpr.SAsyncResult.

    This can take an additional id value allowing to distinguish different
    workers. If it is set, the results are stored in separete queues and
    callbacks are invoked accordingly.
    """
    def __init__(self, id=None):
        multiprocessing.SAsyncResult.__init__(self)
        if id is None:
            self._id = None
        else:
            self._id = '{}'.format(id)
        if id:
